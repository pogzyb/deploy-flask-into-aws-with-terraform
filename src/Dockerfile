FROM python:3.7-slim

RUN apt-get update && apt-get install -y wget

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY ./src/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --upgrade pip

COPY ./src/entrypoint.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/entrypoint.sh

COPY ./src/app/ /${APP_HOME}/app
COPY ./src/instance /${APP_HOME}/instance
COPY ./src/run.py /${APP_HOME}

WORKDIR /${APP_HOME}
EXPOSE ${APP_PORT}

ENTRYPOINT ["/bin/bash", "-c", "entrypoint.sh"]
