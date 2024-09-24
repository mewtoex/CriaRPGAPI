import os
from supabase import create_client

url = "https://yzhjsnpriarialevpvpb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6aGpzbnByaWFyaWFsZXZwdnBiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzEzNjM5OSwiZXhwIjoyMDQyNzEyMzk5fQ.MzShIlJ4pnlrVwSgTt5G_p7bKM1NhNYTPIAviiWXEvg"

supabase = create_client(url, key)

def loginBD(user, password):
    try:
        response = supabase.table('user').select("id").eq('login', user).eq('senha', password).execute()
        return response.data
    except Exception as e:
        print(f"Erro ao conectar ao Supabase: {e}")
        return None
