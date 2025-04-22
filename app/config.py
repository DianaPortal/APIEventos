import os

class Config:
    # variable de entorno DATABASE_URL - conectar a la base de datos.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///eventos.db')  # Si no está definida, usa SQLite local
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #  SECRET_KEY 
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave-secreta-por-defecto')
