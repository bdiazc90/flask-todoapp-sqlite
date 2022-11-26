from app import create_app
# from app.db import db

app = create_app()


# # Crear la tabla por unica vez:
# db.init_app(app)
# with app.app_context():
#     db.create_all() # Buscar las clases que heredan de "db.Model" y las va a crear en caso no existan.