# Gitlab Runner Setup

## Install Runner

This step is already handled by the Compose file in this directory. For the related instructions
see [Docker image installation and configuration](https://docs.gitlab.com/runner/install/docker.html#docker-image-installation-and-configuration).

## Register Runner

After installing a runner you must register it. See the [Docker related instructions](https://docs.gitlab.com/runner/register/index.html#docker).
The runner can be registered as a specific or shared runner. The former executes jobs for specified project(s), while the latter executes
jobs for all projects without specific runners. Using the Gitlab runner service as a development tool, I chose to register it as a specific
runner:

```shell
docker run --rm -t -i -v $PWD/config:/etc/gitlab-runner --name gitlab-runner gitlab/gitlab-runner register
```

Then answer the setup options. Note:

1) To get the `gitlab-ci token`:

    * visit the project you want to register the runner for
    * go to **Settings** > **CI /CD**
    * expand **Runners settings**
    * the token is displayed in the third option under "How to setup a specific Runner for a new project".

1) Can leave 'tags' blank.
1) Choose 'docker' as the executor.
1) Choose 'alpine:latest' as the default Docker image.