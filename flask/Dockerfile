FROM python:3.7.1-stretch

ENV REDIS_PW = "root"
ENV MONGO_USERNAME = "root"
ENV MONGO_PASSWORD = "example"

WORKDIR /code

COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code

CMD ["uwsgi", "wsgi.ini"]
