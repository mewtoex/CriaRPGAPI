from flask import Blueprint, jsonify, request
from app.database import connect_to_db
import privete

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/execute-query', methods=['POST'])
def execute_query():
    query = request.json.get('query')
    conn = connect_to_db()
    
    if conn:
        cursor = conn.cursor()
        try:
            sql_query, params = privete.query2(0)
            cursor.execute(sql_query, params)
            columns = [column[0] for column in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return jsonify(results)
        except Exception as e:
            return jsonify({"message": f"Erro ao executar a query: {e}"}), 400
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({"message": "Falha na conexão."}), 500