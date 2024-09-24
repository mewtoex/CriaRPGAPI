from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

def connect_to_db():
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return supabase
    except Exception as e:
        print(f"Erro ao conectar ao Supabase: {e}")
        return None