import os
from supabase import create_client

 
def query():
    response = supabase.table('piveteType').select("*").execute()
    return response.data

def query1(id):
    response = supabase.table('piveteType').select("*").eq('id', id).execute()
    return response.data