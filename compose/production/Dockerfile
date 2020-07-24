FROM python:3.6.11
ENV PYTHONUNBUFFERED 1
ENV ENVTYPE=production
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ADD /requirements/$ENVTYPE.txt $APP_HOME
RUN pip install -r /home/app/web/$ENVTYPE.txt; mkdir /log; 
COPY /src/ $APP_HOME
CMD ["gunicorn","wsgi:app","-b","0.0.0.0:8011","--log-level=info"]

    



