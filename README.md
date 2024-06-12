# FastAPI, Poetry, Docker Boilerplate

## Requirements

- [Poetry](https://python-poetry.org/) for Python package and environment management.
- [FastAPI](https://fastapi.tiangolo.com/) for Python RESTful API.
- [Docker](https://www.docker.com/) for containerization and deployment.

## Prerequisites

- Install [Poetry](https://python-poetry.org/) following the official documentation.
- Install [Docker](https://www.docker.com/) following the official documentation.

## Quickstart

### Local Development

Create Poetry virtual environment by installing the project dependencies specified in `pyproject.toml` and `poetry.lock`.

```sh
poetry install
```

Run FastAPI development mode under Poetry virtual environment.

```sh
poetry run fastapi dev app/main.py
```

Alternatively, activate the Poetry nested shell and run FastAPI development mode. Exit the shell with `exit`.

```sh
poetry shell
fastapi dev app/main.py
```

By default the app services at http://127.0.0.1/, which is the localhost. The Swagger API documentation is available at http://127.0.0.1:8000/docs/.

> [!TIP]
> The FastAPI local development mode has auto-reload enabled by default, so it will automatically reload the server when code changes are made. This is resource intensive and should only be used for development.

### Dockerization

Build the Docker image.

```sh
docker image build -t fastapi-poetry-docker .
```

Run the Docker container.

```sh
docker run --rm -p 8000:80 fastapi-poetry-docker
```

Alternatively, build and run the Docker container with Docker compose.

```sh
docker compose up
```

The current configuration let the app services at http://0.0.0.0:8000/. The Swagger API documentation is available at http://0.0.0.0:8000/docs/.



## Build from Scratch

### Create Poetry Environment

#### Initialize pyproject.toml

Create a basic `pyproject.toml` file in the current directory.

```sh
cd [directory]
poetry init
```

The command will guide the process of creating the `pyproject.toml` config. Set python version as `^3.11`. Provide the following packages as main dependencies.

- `fastapi`
- `pydantic-settings`

Manually add the following config to `pyproject.toml` to use Poetry only for dependency management but not for packaging.

```toml
[tool].poetry
package-mode = false
```

**Optional:** Add dependencies that are only needed for test and development, for example `pytest` and `ipykernel`.

```sh
poetry add pytest ipykernel --group dev
```

#### Install Project Dependencies

Install the project dependencies specified in `pyproject.toml` and create Poetry virtual environment.

```sh
poetry install
```

> [!TIP]
> List all the environments with the current project. The newly created environment should be shown and marked as `Activated`.
> 
> ```sh
> poetry env list
> ```
>
> Get basic information about the currently activated environment.
> ```
> poetry env info
> ```
>
> List all the available packages installed in the environment.
> 
> ```sh
> poetry show
> ```


