FROM python:3.9-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
