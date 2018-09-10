FROM puckel/docker-airflow:1.10.0-2

USER root

# Install Airflow DAG dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt  \
    && rm -rf /requirements.txt

USER airflow