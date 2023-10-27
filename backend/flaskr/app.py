from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import os
from .routes.routes import setup_routes
from .models.models import init_app, db
from flask_migrate import Migrate

def create_app() -> Flask:
    app = Flask(__name__)
    api = Api(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
    app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
    CORS(app, 
         origins=["http://localhost:3000", os.environ.get("AUTH0_DOMAIN")],
         methods=['GET', 'POST', 'PUT', 'OPTIONS', 'DELETE'],
         allow_headers=['Origin', 'Content-Type', 'Accept']
         )
    init_app(app)
    Migrate(app, db)
    setup_routes(app, api)
    return app
