from app.app import app
from app.models import db


# Crear las tablas de la base de datos
with app.app_context():
    db.create_all()
    print("Base de datos y tablas creadas exitosamente!")
