from flask import Flask, jsonify, request
import pyodbc
import privete

app = Flask(__name__)

# Função para conectar ao SQL Server
def connect_to_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=TOBI-PC\\SQLEXPRESS;' 
            'DATABASE=CRIARPG;'
            'Trusted_Connection=yes;'
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Rota exemplo para executar uma query
@app.route('/execute-query', methods=['POST'])
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)