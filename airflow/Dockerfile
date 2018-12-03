FROM puckel/docker-airflow

USER root

# Mirror credentials of the host user to run the container.
# ARG UNAME=django  # Using static name since COPY --chown doesn't support ARGs!
ARG UID=1000
ARG GID=20

# Update permissions on airflow user files
# -xdev option ignores proc related errors, see https://askubuntu.com/a/1038226/567843
RUN find / -xdev -user airflow -exec chown -h $UID:$GID {} \;

# Update existing airflow user
RUN usermod --non-unique --uid $UID airflow && groupmod --non-unique --gid $GID airflow


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