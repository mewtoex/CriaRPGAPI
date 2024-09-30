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
    response = supabase.table('tecnicas').select("*").like('prerequisito', pre).execute()
    return response.data

