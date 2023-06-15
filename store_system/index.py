import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from pymongo import MongoClient

load_dotenv()
mongo_client = os.getenv('mongo_client')
mongo_db = os.getenv('mongo_db')
mongo_collection = os.getenv('mongo_collection')
mongo_sequence_collection = os.getenv('mongo_sequence_collection')

app = Flask(__name__)
client = MongoClient(mongo_client)
db = client[mongo_db]
collection = db[mongo_collection]
sequence_collection = db[mongo_sequence_collection]


def get_next_sequence(collection_name):
    sequence_doc = sequence_collection.find_one_and_update(
        {'_id': collection_name},
        {'$inc': {'sequence_value': 1}},
        upsert=True,
        return_document=True
    )
    return sequence_doc['sequence_value']


@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = list(collection.find({}, {'_id': False}))
    return jsonify(produtos)


@app.route('/produtos', methods=['POST'])
def add_produto():
    produto = request.get_json()
    produto['id'] = get_next_sequence(mongo_collection)
    collection.insert_one(produto)
    return jsonify({'message': 'Produto adicionado com sucesso!', 'id': produto['id']})


@app.route('/produtos/<id>', methods=['GET', 'PUT', 'DELETE'])
def produto(id):
    if request.method == 'GET':
        produto = collection.find_one({'id': int(id)}, {'_id': False})
        if produto:
            return jsonify(produto)
        else:
            return jsonify({'message': 'Produto não encontrado.'}), 404
    elif request.method == 'PUT':
        novo_produto = request.get_json()
        collection.update_one({'id': int(id)}, {'$set': novo_produto})
        return jsonify({'message': 'Produto atualizado com sucesso!'})
    elif request.method == 'DELETE':
        collection.delete_one({'id': int(id)})
        return jsonify({'message': 'Produto removido com sucesso!'})


if __name__ == '__main__':
    app.run(debug=True)