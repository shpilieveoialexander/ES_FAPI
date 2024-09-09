# ES_FastAPI

____

## About:

ES_FastAPI research and testing project to study ElasticSearch
___


## Features:

- Full **Docker** integration (Docker based).

-  **Docker Compose** integration and optimization.

-  **Deploying ready** Python web server using Uvicorn and Gunicorn.

- Python [FastAPI](https://github.com/tiangolo/fastapi) backend:
  * **Fast**: Very high performance.
  * **Intuitive**: Great editor support. Completion everywhere. Less time debugging.
  * **Easy**: Designed to be easy to use.
  * **Short**: Minimum code duplication.
  * **Robust**: Production-ready code. With interactive documentation.
  * **Standards-based**: Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification)and [JSON Schema](http://json-schema.org/).
  * [Many other features](https://fastapi.tiangolo.com/features/) including automatic validation, serialization, interactive documentation, authentication with OAuth2 JWT tokens, etc.

-  **Secure password** hashing by default.

-  **JWT token** authentication.

-  **SQLAlchemy** models.

-  **Alembic** migrations.

-  **CORS** (Cross Origin Resource Sharing).

- REST backend tests based on **pytest** or **unittest** python libraries, integrated with Docker, so you can test the full API interaction, independent on the database. As it runs in Docker, it can build a new data store from scratch each time.

-  **JWT Authentication** handling.

- Docker multi-stage building, so your project will have the less size.
___


## Project setup:

To start project machine must have:

* [docker](https://docs.docker.com/engine/install/) - The virtual environment to set up project

* [docker-compose](https://docs.docker.com/compose/install/) - The additional util to manipulate of all services inside

### Project setup steps:

1) Open directory with `docker-compose` and `.env` file

2) Open `.env` file and change values

3) Write commands:

3.1 Build base dockerfile:

```shell
docker build -f Dockerfile -t base_dockerfile .
```

3.2 Build containers:

```shell
docker-compose -f <docker-compose file> build
```

3.3 Run project:

```shell
docker-compose -f <docker-compose file> up -d
```
___


## Environment:
### The .env files

The `.env` file is the one that contains all your configurations, generated keys and passwords, etc.


### Environments:

#### Backend

-  **BACKEND_CORS_ORIGINS** - A list with HTTP headers that allow the server to specify any source (domain, schema, or port) other than its own, from which the browser can allow resources to be loaded.

-  **PROJECT_NAME** - Project's name

-  **SECRET_KEY** - This key is used to encrypt all sensitive data and makes your project more secure. Кeep the secret key used in production secret!

-  **SUPERUSER_EMAIL** - Default superuser email

-  **SUPERUSER_PASSWORD** - Default superuser password

-  **SUPERUSER_USERNAME** - Default superuser username

-  **SUPERUSER_FIRST_NAME** - Default superuser firstname

-  **SUPERUSER_LAST_NAME** - Default superuser lastname

-  **DEFAULT_TIME_ZONE** - That timezone will be used by default (example: `"Europe/Kiev"`)

#### Postgres

-  **POSTGRES_SERVER** - Database server

-  **POSTGRES_USER** - Database user

-  **POSTGRES_PASSWORD** - Database user password

-  **POSTGRES_DB** - Database name

___


## Project backend documentation

After project is start, frontend developers can use endpoints documentation:

Redoc:

``
  <domain_name.com>/redoc/
``

Swagger:

``
  <domain_name.com>/swagger/
``
___


## Additional commands:

Stop project:

```
docker-compose -f <docker-compose file> stop
```

Down containers:

```
docker-compose -f <docker-compose file> down
```

Down containers and delete volumes (`all data from database will be deleted!`):

```
docker-compose -f <docker-compose file> down -v
```
___


## Bash scripts:

Start project:

```
docker-compose -f <docker-compose file> run --rm <backend_service> ./bash_scripts/start.sh
```

Format code style:

```
docker-compose -f <docker-compose file> run --rm <backend_service> ./bash_scripts/format.sh
```

Run project tests:

```
docker-compose -f <docker-compose file> run --rm <backend_service> ./bash_scripts/test.sh
```

Run project tests and build coverage:

```
docker-compose -f <docker-compose file> run --rm <backend_service> ./bash_scripts/coverage_test.sh
```
___


## Project technologies:

- [docker](https://docs.docker.com/) - is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.


- [docker-compose](https://docs.docker.com/compose/) - Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about all the features of Compose, see [the list of features](https://docs.docker.com/compose/#features).


- [python](https://docs.python.org/3.11/) - is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.


- [FastAPI](https://fastapi.tiangolo.com/) - is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
___


## Project requirements

### For Databases:
* **alembic** - is a lightweight database migration tool for usage with the [SQLAlchemy](https://www.sqlalchemy.org/) Database Toolkit for Python. 
* **postgis** - extends the capabilities of the [PostgreSQL](https://postgresql.org/) relational database by adding support storing, indexing and querying geographic data
* **psycopg2-binary** - the most popular PostgreSQL database adapter for the Python programming language.
* **redis** - The open source, in-memory data store used by millions of developers as a database, cache, streaming engine, and message broker.
* **SQLAlchemy** - is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
* **SQLAlchemy-Utils** - provides custom data types and various utility functions for SQLAlchemy.
* **tenacity** - is a general-purpose retrying library to simplify the task of adding retry behavior to just about anything.

### For Backend:
* **email-validator** - A robust email address syntax and deliverability validation library for Python 3.7+
* **fastapi** - is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
* **fastapi-pagination** - is a Python library designed to simplify pagination in FastAPI applications.
* **pydantic** - Data validation and settings management using Python type hints.
* **python-jose** - A JOSE implementation in Python
* **ujson** - is an ultra fast JSON encoder and decoder written in pure C with bindings for Python 3.7+.
* **uvicorn** - is an ASGI web server implementation for Python.

### For Codestyle
* **autoflake** - removes unused imports and unused variables from Python code. It makes use of [pyflakes](https://pypi.org/pypi/pyflakes) to do this.
* **black** - is the uncompromising Python code formatter.
* **flake8** - is a wrapper around tools as: (**PyFlakes**, **pycodestyle** and **Ned Batchelder’s McCabe script**)
* **isort** - is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.
