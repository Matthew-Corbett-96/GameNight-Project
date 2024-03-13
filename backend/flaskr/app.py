from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate
import os
from .router.routes import setup_routes
from .models.models import init_app, db
from .schedule import create_scheduler
from logging import getLogger


def create_app():
    logger = getLogger('RootLogger')
    app = Flask(__name__)
    api = Api(app)  # TODO: Add Prefix 'api/v1/' to api routes
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:postgrespw@localhost:5432/postgres"
    )
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
    migrate = Migrate(app=app, db=db, directory="migrations", render_as_batch=True)
    scheduler = create_scheduler(app)
    setup_routes(app, api)
    logger.info("App Init Complete")
    return app
