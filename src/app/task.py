from app import create_celery
from utils.logging import logger

celery_app = create_celery()

@celery_app.task(max_retries=3,time_limit=7200)
def periodic():
    print('Hi! from periodic_task')

    
