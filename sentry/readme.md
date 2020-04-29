# Sentry

Deploys a local Sentry server for realtime event logging and aggregation.

## Quick Start

See [Sentry DockerHub](https://hub.docker.com/_/sentry/) for complete setup instructions.

### Create Docker Network

First, create a Docker Network to allow other local Compose stacks to discover Sentry:

```shell
docker network create sentry_default
```

Note: To connect other dev environments to Sentry use:

```yml
version: "3"
services:
  app:
    build: .
    image: bookshelf
    command: ./manage.py runserver_plus 0.0.0.0:8000
    environment:
      SENTRY_DSN: http://90cd262318fd4904b735809e4fcde4fc@sentry:9000/1
    networks:
      - default
      - sentry
    external_links:
      - sentry_web_1:sentry

networks:
  sentry:
    external:
      name: sentry_default
```

### Run Upgrade Command

Next, running the following command which sets up Sentry's database:

```
docker-compose run sentry upgrade
```

You will be asked to create a superuser during this process. If you say no, you can create one after using:

```
docker-compose run sentry createuser
```

### Start App

Now, you should be able to run:

```
docker-compose up -d
```

## Warning

Note: The `SENTRY_SECRET_KEY` hardcoded into the Compose file MUST NOT BE USED for production.

You can generated one by running:

```
 docker run --rm sentry config generate-secret-key
```
