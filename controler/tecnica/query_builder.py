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
    if not isinstance(pre, dict):
        return []
 
    if 'chassi' in pre and pre['chassi'] is not None:
        chassi = pre.get('chassi', '')
        query = query.or_(
            f"chassi.like.%{chassi}%,chassi.eq.''"
        )
    if 'elemento' in pre and pre['elemento'] is not None:
        elemento = pre.get('elemento', '')
        query = query.or_(
            f"elemento.like.%{elemento}%,elemento.eq.''"
        )
    if 'rank' in pre and pre['rank'] is not None:
        rank = pre.get('rank', '')
        query = query.or_(
            f"rank.like.%{rank}%,rank.eq.''"
        )

    if 'chassi' in pre and pre['chassi'] is not None:
        chassi = pre.get('chassi', '')
        query_chassi_and_elemento_null = supabase.table('tecnicas').select("*")\
        .eq('chassi', chassi)\
        .is_('elemento', None)

    if 'elemento' in pre and pre['elemento'] is not None:
        elemento = pre.get('elemento', '')
        query_elemento_and_chassi_null = supabase.table('tecnicas').select("*")\
        .eq('elemento', elemento)\
        .is_('chassi', None)
   
        query_prerequisito_null1 = supabase.table('tecnicas').select("*")\
        .eq('prerequisito', 0)\

    
    response_filter = query.execute()
    response_chassi = query_chassi_and_elemento_null.execute()
    response_pre = query_prerequisito_null1.execute()
    response_elemento = query_elemento_and_chassi_null.execute()
    response = response_pre.data + response_chassi.data + response_elemento.data + response_filter.data
    return response

