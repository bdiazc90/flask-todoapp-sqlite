from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Importar los blueprint que queremos unir a nuestra app:
from app.routes.tasks import task_router

def create_app():
    app = Flask(__name__)
    # Vamos a darle parametros de configuracion
    app.config.from_object(Config)
    # Registrar sus módulos de Blueprint:
    app.register_blueprint(task_router)
    # Vamos a crear la instancia de la DB para las migraciones:
    db = SQLAlchemy(app)
    return app