from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import os
from .api.routes import setup_routes
from .models.models import init_app, db
from flask_migrate import Migrate

def create_app() -> Flask:
    app = Flask(__name__)
    api = Api(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    CORS(app, 
         origins=[os.environ.get("CLIENT_ORIGIN_URL"), os.environ.get("AUTH0_DOMAIN")],
         methods=['GET', 'POST', 'PUT', 'OPTIONS', 'DELETE'],
         allow_headers=['Origin', 'Content-Type', 'Accept', 'Authorization', 'X-Requested-With', 'x-auth-token', 'Access-Control-Allow-Origin', 'Access-Control-Allow-Headers', 'Access-Control-Allow-Methods']
         )
    init_app(app)
    Migrate(app, db)
    setup_routes(app, api)
    return app
