FROM python:3.12.3

WORKDIR /secretapp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /secretapp/

RUN POETRY_VIRTUALENVS_CREATE=false poetry install

COPY ./app /secretapp/app

CMD ["fastapi", "run", "--port", "80"]