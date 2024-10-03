import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()

def tecnica_list():
    response = supabase.table('tecnica').select("*").execute()
    return response.data
    
def save_tecnica(tecnica):
    supabase.table('tecnica').insert(vars(tecnica)).execute()

def update_tecnica(tecnica):
    supabase.table('tecnica').update(vars(tecnica)).eq('id', tecnica.id).execute()

def tecnica_list_filter(pre):
    query = supabase.table('tecnicas').select("*")

    if pre.get('chassi') is not None: 
        chassi = pre.get('chassi', '')
        query = query.or_(
            f"chassi.like.%{chassi}%,chassi.eq.''"
        )
    
    if pre.get('elemento') is not None:  
        elemento = pre.get('elemento', '')
        query = query.or_(
            f"elemento.like.%{elemento}%,elemento.eq.''"
        )
        
    if pre.get('rank') is not None: 
        rank = pre.get('rank', '')
        query = query.or_(
            f"rank.like.%{rank}%,rank.eq.''"
        )

    response = query.execute()
    return response.data

