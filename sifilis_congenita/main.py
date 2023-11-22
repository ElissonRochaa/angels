import logging
from flask import Flask, request
from flask import jsonify
import datetime
import decimal
import json

from service import basic_service, complementary_service

from flask_cors import CORS

app = Flask(__name__)

"""
CORS function is to avoid No 'Access-Control-Allow-Origin' error
"""
CORS(app)


licencas_validas = {
    "123456": {"status": "ativo", "cliente": "Empresa A"},
    "789012": {"status": "inativo", "cliente": "Empresa B"}
}

@app.route('/verificar_licenca', methods=['POST'])
def verificar_licenca():
    # Recebe o código de licença do corpo da solicitação POST
    codigo_licenca = request.form.get('codigo_licenca')

    # Verifica se o código de licença está presente
    if not codigo_licenca:
        return jsonify({"error": "Código de licença não fornecido"}), 400

    # Verifica se o código de licença é válido
    if codigo_licenca in licencas_validas:
        info_licenca = licencas_validas[codigo_licenca]
        return jsonify({"status": info_licenca["status"], "cliente": info_licenca["cliente"]})
    else:
        return jsonify({"error": "Código de licença inválido"}), 403


@app.route('/')
def hello():
    """webserice test method
    """
    return 'Welcome to ANGELS - Congenital Syphilis', 200

@app.route('/basic', methods=['POST'])
def basic_model():
    dados = request.get_json()

    dicionario = {}
    for key, value in dados.items():
        dicionario[key] = value

    result = basic_service(dicionario)
    
    #status, predict = basic_service(dados)

    #Ajuste para responder
    if result == True:
        return "Deu certo", 200
    else:
        return result, 403
    #return jsonify(response)

@app.route('/complementary', methods=['POST'])
def complementary_model():
    dados = request.get_json()
    # model = Model()
    # classificacao, probabilidade, explainer = model.predict(dados)
    
    # proba = [{'nome':'Dengue', 'probabilidade':probabilidade[1]}, {'nome':'Chikungunya', 'probabilidade':probabilidade[0]}, {'nome':'Inconclusivo', 'probabilidade':probabilidade[2]}]
    # response = {'status': 0, 'classificacao': classificacao, 'probabilidades': proba, 'explainer': explainer.to_dict()}
    
    # return jsonify(response)

# Função para lidar com erros 404
@app.errorhandler(404)
def page_not_found(error):
    return 'Erro: caminho não encontrado', 404


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    #app.run(host='192.168.0.58', port=8080, debug=True, processes=4, threaded=True)
    #app.run(threaded=True,debug=True)
    #model = Model()
    app.run(host='0.0.0.0', port=5000)
## [END app]
