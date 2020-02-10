import os
import sys
from celery.schedules import crontab

class Config:
    pass

class Celery:
    BROKER_URL = os.getenv('CELERY_BROKER_URL','redis://redis:6379/0')
    CELERY_TIMEZONE='America/Santiago'
    CELERY_ENABLE_UTC=True
    CELERYBEAT_SCHEDULE = {
        'periodic_task-every-minute': {
            'task': 'app.task.periodic',
            'schedule': crontab(minute=15, hour='15')
        }
    }



