from app import create_app
from app.models.db import db

app = create_app()

# Crear la tabla por unica vez:
db.init_app(app)
with app.app_context():
    db.create_all()

