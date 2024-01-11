FROM python:3.10.9-slim as builder

ENV PATH /opt/venv/bin:$PATH
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /opt
#
RUN python -m pip install --upgrade pip \
    && apt-get update \
    && apt-get -y install gcc python3-dev \
    && apt-get install -y --no-install-recommends git
RUN apt-get install unzip
RUN apt-get -y install build-essential 
#
#
RUN python -m venv venv
RUN pip install -U pip setuptools
RUN pip install poetry==1.2.2
RUN /opt/venv/bin/python -m pip install ipykernel -U --force-reinstall
#
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

