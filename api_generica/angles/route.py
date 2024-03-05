from angles import app
from flask import jsonify, request

@app.route('/')
def inicial():
    return "Bem-vindo a nossa API"

# Rota para retornar uma lista de itens
@app.route('/api/items', methods=['GET'])
def get_items():
    items = ['item1', 'item2', 'item3']
    return jsonify({'items': items})

# Rota para adicionar um novo item
@app.route('/api/items', methods=['POST'])
def add_item():
    dados = request.get_json()
    print(dados['idade'])
    # Lógica para adicionar um novo item
    return jsonify({'message': 'Item adicionado com sucesso!'})

# Rota para atualizar um item existente
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # Lógica para atualizar o item com o ID fornecido
    return jsonify({'message': f'Item com o ID {item_id} foi atualizado'})

# Rota para excluir um item
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # Lógica para excluir o item com o ID fornecido
    return jsonify({'message': f'Item com o ID {item_id} foi excluído'})
