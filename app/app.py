from flask import Flask, jsonify, request
from app.models import db, Evento
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Endpoint para obtener la lista de eventos
@app.route('/api/eventos', methods=['GET'])
def get_eventos():
    eventos = Evento.query.all()
    eventos_schema = [
        {
            'id': evento.id,
            'titulo': evento.titulo,
            'fecha': evento.fecha,
            'hora': evento.hora,
            'descripcion': evento.descripcion,
            'ubicacion': evento.ubicacion,
            'latitud': evento.latitud,
            'longitud': evento.longitud
        }
        for evento in eventos
    ]
    return jsonify(eventos_schema)

# Endpoint para agregar un nuevo evento
@app.route('/api/eventos', methods=['POST'])
def add_evento():
    data = request.get_json()
    nuevo_evento = Evento(
        titulo=data['titulo'],
        fecha=data['fecha'],
        hora=data['hora'],
        descripcion=data['descripcion'],
        ubicacion=data['ubicacion'],
        latitud=data['latitud'],
        longitud=data['longitud']
    )
    db.session.add(nuevo_evento)
    db.session.commit()
    return jsonify({'message': 'Evento creado exitosamente!'}), 201

# Endpoint para actualizar un evento existente
@app.route('/api/eventos/<int:id>', methods=['PUT'])
def update_evento(id):
    evento = Evento.query.get(id)
    if not evento:
        return jsonify({'error': 'Evento no encontrado'}), 404

    data = request.get_json()
    evento.titulo = data.get('titulo', evento.titulo)
    evento.fecha = data.get('fecha', evento.fecha)
    evento.hora = data.get('hora', evento.hora)
    evento.descripcion = data.get('descripcion', evento.descripcion)
    evento.ubicacion = data.get('ubicacion', evento.ubicacion)
    evento.latitud = data.get('latitud', evento.latitud)
    evento.longitud = data.get('longitud', evento.longitud)

    db.session.commit()
    return jsonify({'message': 'Evento actualizado exitosamente!'})

# Endpoint para eliminar un evento existente
@app.route('/api/eventos/<int:id>', methods=['DELETE'])
def delete_evento(id):
    evento = Evento.query.get(id)
    if not evento:
        return jsonify({'error': 'Evento no encontrado'}), 404

    db.session.delete(evento)
    db.session.commit()
    return jsonify({'message': 'Evento eliminado exitosamente!'})


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
