from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'greg.brown',
    'start_date': datetime(2018, 7, 9),
    'retries': 0,
    'catchup': False
}


dag = DAG('simple_dag',
          default_args=default_args,
          # schedule_interval='* * * * 1-5'
          schedule_interval=timedelta(seconds=30)
          )

t1 = BashOperator(
    task_id='simple_task',
    dag=dag,
    bash_command='''echo "Simple task complete: {{ ds }}"'''
)