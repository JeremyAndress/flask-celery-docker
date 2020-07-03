FROM python:3.6
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD /requirements/local.txt $APP_HOME

RUN export https_proxy=http://10.46.0.210:3128; \
    export http_proxy=http://10.46.0.210:3128; \
    pip install gunicorn; \
    pip install -r /home/app/web/local.txt; mkdir /log;
