ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --deploy --system
COPY . /code

EXPOSE 8000

ENTRYPOINT ["./start.sh"]
