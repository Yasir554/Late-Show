from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from .extensions import db
from .config import Config
from .routes import register_routes

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    api = Api(app)
    register_routes(api)

    return app