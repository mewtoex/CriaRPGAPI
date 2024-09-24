from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("https://yzhjsnpriarialevpvpb.supabase.co/")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6aGpzbnByaWFyaWFsZXZwdnBiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzEzNjM5OSwiZXhwIjoyMDQyNzEyMzk5fQ.MzShIlJ4pnlrVwSgTt5G_p7bKM1NhNYTPIAviiWXEvg")

def connect_to_db():
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return supabase
    except Exception as e:
        print(f"Erro ao conectar ao Supabase: {e}")
        return None