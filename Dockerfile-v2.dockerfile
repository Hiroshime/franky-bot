FROM python:3

RUN mkdir /app
WORKDIR /app
ADD . /app/

