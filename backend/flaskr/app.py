from flask import Flask
from flask_restful import Api
import os
from .routes.routes import setup_routes
from .models.models import init_app, db
from flask_migrate import Migrate

def create_app() -> Flask:
    app = Flask(__name__)
    api = Api(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
    init_app(app)
    Migrate(app, db)
    setup_routes(app, api)
    return app
