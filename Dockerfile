FROM python:3.7-slim

RUN apt-get update && apt-get install -y wget

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY . /code
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["dockerize", "-wait", "tcp://postgres:5432", "-timeout", "60s", "python", "-u", "run.py"]
