import logging
from sys import stdout
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate
from celery.schedules import crontab
import os
from logging import getLogger
from .router.routes import setup_routes
from .models.models import init_app, db
from flaskr.utils import celery_init_app

def create_app():
    logging.basicConfig(stream=stdout, level=logging.INFO)
    logger = getLogger(__name__)
    app = Flask(__name__)
    api = Api(app)  # TODO: Add Prefix 'api/v1/' to api routes
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:postgrespw@db:5432/postgres"
    )
    app.config["CELERY_CONFIG"] = {
        "broker_url": os.environ.get("CELERY_BROKER_URL", "redis://redis"),
        "result_backend": os.environ.get("CELERY_RESULT_BACKEND", "redis://redis"),
        "beat_schedule": {
            "send_day_before_message": {
                "task": "flaskr.tasks.send_day_before_message",
                "schedule": crontab(minute="*/1"),
            },
            "send_day_of_message": {
                "task": "flaskr.tasks.send_day_of_message",
                "schedule": crontab(minute="*/5"),
        },
      }
    }
    CORS(
        app,
        origins=[
            os.environ.get("CLIENT_ORIGIN_URL"),
            os.environ.get("AUTH0_DOMAIN"),
            # os.environ.get("TWILIO_DOMAIN"),
        ],
        methods=["GET", "POST", "PUT", "OPTIONS", "DELETE"],
        allow_headers=[
            "Origin",
            "Content-Type",
            "Accept",
            "Authorization",
            "X-Requested-With",
            "x-auth-token",
            "Access-Control-Allow-Origin",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Methods",
        ],
    )

    # Initialize the database connection and create tables
    init_app(app)
    celery = celery_init_app(app)
    celery.set_default()
    migrate = Migrate(app=app, db=db, directory="migrations", render_as_batch=True)
    setup_routes(app, api)
    logger.info("App Init Complete")
    return app, celery
