# titanic_examp

This project was generated using fastapi_template. It is written using the combination of the FastAPI framework, SQLAlchemy framework, Alembic for migrations, and SQLite.

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m titanic_examp
```

This will start the server on the configured host.

You can find swagger documentation at `/docs`.

You can read more about poetry here: https://python-poetry.org/

## Project structure

```bash
$ tree "titanic_examp"
notebooks # contains the solved ubo.ipynb file for the second challenge.
titanic_examp
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   ├── migrations # Alembic migrations
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Loading the Passengers List

In order to load the database, either make a `PUT` REST request to "http://127.0.0.1:8000/titanic/" or follow the instructions below with a browser to load the passenger list.

#### Instructions using Swagger
Visit http://localhost:8000/docs , scroll to "PUT `/titanic/` Create Titanic Model" in orange. "Try it out". Then execute. Each press of execute should load the list of 891 passengers from the `titanic.csv` in the `titanic_examp/static` folder.

At that point, you can read the passengers using `GET /titanic/`.

The passengers list could be permanently migrated into the database if desired using alembic, though that might involve their personal identifiable information being committed to the code base, undesirable in some similar situations.

## Use the titanic API

## Configuration

This application can be configured with environment variables. It should be optional.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "TITANIC_EXAMP_" prefix.

An example of .env file:
```bash
TITANIC_EXAMP_RELOAD="True"
TITANIC_EXAMP_PORT="8000"
TITANIC_EXAMP_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/


## Running tests

### Redoc documentation is at:
http://localhost:8000/redoc

### Swagger documentation is at:
http://localhost:8000/docs

For running tests on your local machine:


1. Run the pytest.
```bash
poetry run pytest -vv .
```

<details>
If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```
</details>

### Migrations, Docker, etc.
<details>

## Migrations

If you want to migrate your database, you should run following commands:
```bash
# To run all migrations until the migration with revision_id.
alembic upgrade "<revision_id>"

# To perform all pending migrations.
alembic upgrade "head"
```

### Reverting migrations

If you want to revert migrations, you should run:
```bash
# revert all migrations up to: revision_id.
alembic downgrade <revision_id>

# Revert everything.
 alembic downgrade base
```

### Migration generation

To generate migrations you should run:
```bash
# For automatic change detection.
alembic revision --autogenerate

# For empty file generation.
alembic revision
```


## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possible bugs);


You can read more about pre-commit here: https://pre-commit.com/

</details>
