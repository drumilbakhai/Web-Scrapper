FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip
RUN pip install pipenv
ADD . /flask-app
WORKDIR /flask-app

ENV SHELL=/bin/bash
RUN pipenv --two
RUN pipenv install --system --deploy --ignore-pipfile

ENTRYPOINT ["python"]
CMD ["app.py"]
