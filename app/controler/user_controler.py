import os
from flask import jsonify, request
from user.query_builder import login_bd, save_user, update_user

def login_controller_user():  
    data = request.get_json()
    user = data.get('user')
    password = data.get('pass')

    if not user or not password:
        return jsonify({"message": "Usuário e senha são obrigatórios."}), 400

    results = login_bd(user, password)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Usuário ou senha inválidos."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_user():  
    data = request.get_json()
    user = data.get('user')
    password = data.get('pass')

    if not user or not password:
        return jsonify({"message": "Usuário e senha são obrigatórios."}), 400

    results = save_user(user, password)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Usuário não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_user():  
    data = request.get_json()
    user = data.get('user')
    password = data.get('pass')

    if not user or not password:
        return jsonify({"message": "Usuário e senha são obrigatórios."}), 400

    results = update_user(user, password)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Usuário não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
