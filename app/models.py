from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    fecha = db.Column(db.String(10), nullable=False)  # 'YYYY-MM-DD'
    hora = db.Column(db.String(5), nullable=False)    # 'HH:MM'
    descripcion = db.Column(db.String(500), nullable=True)
    ubicacion = db.Column(db.String(200), nullable=True)
    latitud = db.Column(db.Float, nullable=True)
    longitud = db.Column(db.Float, nullable=True)

    def __init__(self, titulo, fecha, hora, descripcion, ubicacion, latitud, longitud):
        self.titulo = titulo
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.latitud = latitud
        self.longitud = longitud
