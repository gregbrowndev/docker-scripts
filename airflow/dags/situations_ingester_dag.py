from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.slack_operator import SlackAPIPostOperator, SlackAPIOperator
import pendulum

from datetime import datetime, timedelta

from slack_file_upload_operator import SlackAPIFileUploadOperator

# This DAG is timezone aware and will be scheduled in UK timezone
local_tz = pendulum.timezone("Europe/London")

default_args = {
    'owner': 'greg.brown',
    'depends_on_past': False,
    'start_date': datetime(2018, 9, 9, tzinfo=local_tz),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
    'catchup': False
}
# Following are defaults which can be overridden later on

project_dir = '/apps/situations_ingestor/'

SLACK_TOKEN = 'xoxp-3442381301-107001513984-395867889012-c91400165f0df67c4d3d24b961ba4140'

# Scheduled to run at 10am weekdays Mon-Fri (note Airflow schedules at the end of the interval so cron is set to 9am)
dag = DAG('SituationIngester',
          default_args=default_args,
          catchup=False,
          schedule_interval='0 9 * * 1-5'
          # schedule_interval='*/10 * * * 1-5'
          # schedule_interval=None
          )

install_deps = BashOperator(
    task_id='install_deps',
    bash_command='cd {{ params.project_dir }} && pipenv install',
    params={'project_dir': project_dir},
    dag=dag)

clear_data = BashOperator(
    task_id='clear_data',
    bash_command='rm -rf {{ params.project_dir }}disruption_data_*',
    params={'project_dir': project_dir},
    dag=dag)

zip_data = BashOperator(
    task_id='zip_data',
    bash_command='''
        cd {{ params.project_dir }} \
        && rm -f disruption_data.zip \
        && zip disruption_data disruption_data_{{ ds }}/*
    ''',
    params={'project_dir': project_dir},
    dag=dag
)


def upload_filename():
    filename = '{project_dir}disruption_data.zip' \
        .format(project_dir=project_dir)
    return open(filename, 'rb')


def upload_title():
    # return 'Disruption Data {timestamp}'\
    #     .format(timestamp=pendulum.now('Europe/London').date())
    return 'Disruption Data'


slack_upload = SlackAPIFileUploadOperator(
    dag=dag,
    task_id='slack_upload',
    token=SLACK_TOKEN,
    # channels='D35JTU0PM',
    channels='CBNRTFRLM',
    username='Greg Brown',
    title=upload_title,
    file=upload_filename,
)

scrapers = ['toronto', 'philly', 'lothian', 'mta', 'west-midlands', 'tfl']

scrapy_command = '''
    echo "Crawling {{ params.scraper }}"
    cd {{ params.project_dir }} && pipenv run \
        scrapy crawl {{ params.scraper }} -o disruption_data_{{ ds }}/{{ params.scraper }}_{{ ds }}.csv -L WARNING
'''

install_deps >> clear_data

for scraper in scrapers:
    t = BashOperator(
        task_id='scrape_%s' % scraper,
        bash_command=scrapy_command,
        params={'scraper': scraper,
                'project_dir': project_dir},
        dag=dag
    )
    clear_data >> t >> zip_data

zip_data >> slack_upload
