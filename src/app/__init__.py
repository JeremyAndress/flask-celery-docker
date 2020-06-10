from flask import Flask
from flask_cors import CORS
from celery import Celery


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    cors = CORS(app, resources={r"*": {"origins": "*"}})
    with app.app_context():
        # Include our Routes
        from . import routes
        #Register Blueprints
        app.register_blueprint(routes.task_bp)

        return app

def create_celery():
    """Initialize celery application."""
    app = Celery('hearth')
    app.config_from_object('config.Celery')

    return app