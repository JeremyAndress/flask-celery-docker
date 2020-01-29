from flask import Blueprint
from flask import request
from datetime import datetime
from utils.logging import logger
task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/', methods=['GET'])
def index():
    return 'Flask Celery Template!!!'

