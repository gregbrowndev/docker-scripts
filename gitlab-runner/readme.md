# Gitlab Runner

## Overview

This provides instructions on various deployments for Gitlab CI Runner. If you are developing a CI-CD pipeline or want to run the tests locally, it is recommended to install the runner directly on your dev machine. This is to avoid complexity in having to bind mount your source code into the container.

## Run Task Locally

With the Runner installed locally, you can use `gitlab-runner exec docker [task]` in your project root and it will execute `[task]` from the local _.gitlab-ci.yml_ file, e.g. `my-build-step`, `test1`, etc.


## Registering the Runner


The runner can be registered as a specific or shared runner. The former executes jobs for specified project(s), while the latter executes
jobs for all projects without specific runners.

When registering a runner using one of the deployment methods below, note:

1) To get the `gitlab-ci token`:

    * visit the project you want to register the runner for
    * go to **Settings** > **CI /CD**
    * expand **Runners settings**
    * the token is displayed in the third option under "How to setup a specific Runner for a new project".

1) Can leave 'tags' blank.
1) Choose 'docker' as the executor.
1) Choose 'alpine:latest' as the default Docker image.


### Using Docker-in-Docker 

To be able to build, test and deploy Docker images we can configure the Runner to use Docker-in-Docker:

```shell
sudo gitlab-runner register -n \
   --url https://gitlab.com/ \
   --registration-token REGISTRATION_TOKEN \
   --executor docker \
   --description "My Docker Runner" \
   --docker-image "docker:stable" \
   --docker-privileged
```

## Linux

See [installation from package manager](https://docs.gitlab.com/runner/install/linux-repository.html):

```bash
 # For Debian/Ubuntu/Mint
 curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash

 # For RHEL/CentOS/Fedora
 curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh | sudo bash
```

Install:

```bash
 # For Debian/Ubuntu/Mint
 sudo apt-get install gitlab-runner

 # For RHEL/CentOS/Fedora
 sudo yum install gitlab-runner
```

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

Register the Runner:

```shell
docker run --rm -t -i -v $PWD/config:/etc/gitlab-runner  gitlab/gitlab-runner register
```
