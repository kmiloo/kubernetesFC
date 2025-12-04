from flask import Flask, request, jsonify

app = Flask(__name__)

# Memoria temporal para guardar votos y quién ya votó
votos = {"OpcionA": 0, "OpcionB": 0, "OpcionC": 0}
ya_votaron = set()

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    usuario_id = data.get('id') # Identificador único del alumno
    voto = data.get('voto')

    # 1. Verificar si ya votó
    if usuario_id in ya_votaron:
        return jsonify({"mensaje": "ERROR: Ya has votado anteriormente."}), 403

    # 2. Registrar voto
    if voto in votos:
        votos[voto] += 1
        ya_votaron.add(usuario_id)
        print(f"!!! NUEVO VOTO RECIBIDO DE {usuario_id} PARA {voto} !!!")
        print(f"Estado actual: {votos}")
        return jsonify({"mensaje": "Voto registrado exitosamente", "resumen": votos}), 200
    else:
        return jsonify({"mensaje": "Opción no válida"}), 400

@app.route('/', methods=['GET'])
def home():
    return jsonify(votos)

if __name__ == '__main__':
    # Escucha en todas las interfaces (0.0.0.0) puerto 5000
    app.run(host='0.0.0.0', port=5000)