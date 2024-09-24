from flask import Blueprint, jsonify, request
from app.services import execute_db_query, userLogin

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/execute-query', methods=['POST'])
def execute_query():
    query_type = request.json.get('query_type')
    id = request.json.get('id')

    try:
        results = execute_db_query(query_type, id)
        return jsonify(results)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@api_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = data.get('user')
    password = data.get('pass')

    if not user or not password:
        return jsonify({"message": "Usuário e senha são obrigatórios."}), 400
       
    results = userLogin(user, password)

    try:
      if results:
            return jsonify(results), 200 
      else:
            return jsonify({"message": "Usuário ou senha inválidos."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500