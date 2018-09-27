# Gitlab Runner

## Overview

This provides a Docker Compose deployment for Gitlab's Runner which can be used to running CI-CD jobs for registered project(s).

Note - I would actually recommend installing the Runner directly, since the containerised runner is more awkward to give access to your code. With the Runner installed locally, you can use `gitlab-runner exec docker [task]` in your project root and it will execute `[task]` from the local _.gitlab-ci.yml_ file.

## Registering the Runner

When registering a runner using one of the deployment methods below, note:

1) To get the `gitlab-ci token`:

    * visit the project you want to register the runner for
    * go to **Settings** > **CI /CD**
    * expand **Runners settings**
    * the token is displayed in the third option under "How to setup a specific Runner for a new project".

1) Can leave 'tags' blank.
1) Choose 'docker' as the executor.
1) Choose 'alpine:latest' as the default Docker image.

## MacOS

Follow the [MacOS installation](https://docs.gitlab.com/runner/install/osx.html).

Install:

```shell
sudo curl --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-darwin-amd64
```

Give it permissions to execute:

```shell
sudo chmod +x /usr/local/bin/gitlab-runner
```

[Register runner](https://docs.gitlab.com/runner/register/index.html#macos):

```shell
gitlab-runner register
```

## Docker Setup
### Install

This step is handled by the Compose file in this directory, simply run:

```shell
docker-compose up -d
```

For the related instructions
see [Docker image installation and configuration](https://docs.gitlab.com/runner/install/docker.html#docker-image-installation-and-configuration).

### Register

After installing a runner you must register it. See the [Docker related instructions](https://docs.gitlab.com/runner/register/index.html#docker).
The runner can be registered as a specific or shared runner. The former executes jobs for specified project(s), while the latter executes
jobs for all projects without specific runners. Using the Gitlab runner service as a development tool, I chose to register it as a specific
runner:

```shell
docker run --rm -t -i -v $PWD/config:/etc/gitlab-runner  gitlab/gitlab-runner register
```
