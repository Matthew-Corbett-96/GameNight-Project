FROM python:3.10.6-alpine3.16
LABEL maintainer="MatthewJCorbett"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app

EXPOSE 8080

# Script to start virtual env, download pip packages, get posgresql client drive, & add new user
# RUN python -m venv /py && \
#     /py/bin/pip install --upgrade pip && \
#     /py/bin/pip install -r /requirements.txt && \
#     adduser --disabled-password --no-create-home app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev &&\
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app

# Adds Path of Virtual Env so we use virt env and not container ver of python
ENV PATH="/py/bin:$PATH"
# Switch to User Created in script above
USER app