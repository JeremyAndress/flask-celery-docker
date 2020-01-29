FROM python:3.6
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD /requirements/local.txt $APP_HOME

RUN pip install gunicorn; \
    pip install -r /home/app/web/local.txt; mkdir /log; 


