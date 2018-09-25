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