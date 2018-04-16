FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip
RUN pip install pipenv
ADD . /flask-app
WORKDIR /flask-app

ENV SHELL=/bin/bash
ENV FLASK_APP=app.py
RUN pipenv --two
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000
CMD ["python", "app.py"]

