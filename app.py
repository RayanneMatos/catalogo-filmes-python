from flask import Flask, request, jsonify, send_from_directory
from catalogo import carregar_dados
from busca import buscar_por_titulo, buscar_por_genero

app = Flask(__name__)
catalogo = carregar_dados()

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/api/filmes', methods=['GET'])
def listar_filmes():
    return jsonify(catalogo)

@app.route('/api/filmes/titulo/<titulo>')
def buscar_por_titulo_api(titulo):
    return jsonify(buscar_por_titulo(catalogo, titulo))

@app.route('/api/filmes/genero/<genero>')
def buscar_por_genero_api(genero):
    return jsonify(buscar_por_genero(catalogo, genero))

if __name__ == "__main__":
    app.run(debug=True)
