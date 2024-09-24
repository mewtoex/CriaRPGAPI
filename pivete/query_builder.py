import os
from supabase import create_client

 
def query():
    response = supabase.table('pivete_type').select("*").execute()
    return response.data

def query1(id):
    response = supabase.table('pivete_type').select("*").eq('id', id).execute()
    return response.data