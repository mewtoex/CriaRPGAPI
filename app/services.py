import os
from app.db import connect_to_db
from pivete.query_builder import query, query1
from user.query_builder import loginBD

def execute_db_query(query_type, id=None):
    try:
        if query_type == "query":
            results = query()
        elif query_type == "query1" and id is not None:
            results = query1(id)
        else:
            raise Exception("Tipo de query inválido ou parâmetros faltando.")

        return results
    except Exception as e:
        raise Exception(f"Erro ao executar a query: {e}")

def userLogin(user, password):  
    results = loginBD(user, password)
    return results
