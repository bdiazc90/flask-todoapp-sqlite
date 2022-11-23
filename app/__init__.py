from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

from app.routes.task import task_router

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(task_router)

    db = SQLAlchemy(app)
    return app
