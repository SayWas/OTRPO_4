FROM python:3.12-slim

RUN mkdir /ftp

WORKDIR /ftp

COPY requirements.txt /ftp

RUN pip install -r requirements.txt

COPY . /ftp
