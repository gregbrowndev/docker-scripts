FROM puckel/docker-airflow:1.10.0-2

USER root

# Install Airflow DAG dependencies
# RUN add-apt-repository main && \
#     add-apt-repository universe && \
#     add-apt-repository restricted && \
#     add-apt-repository multiverse

RUN apt-get update && apt-get install -y --no-install-recommends \
    zip \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt  \
    && rm -rf /requirements.txt

USER airflow

# This ensures the logs directory exists with the airflow user's permissions.
# This allows a volume mount to be bound without creating a new root-owned directory
RUN mkdir -p /usr/local/airflow/logs