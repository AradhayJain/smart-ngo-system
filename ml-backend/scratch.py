import os
from dotenv import load_dotenv
load_dotenv('.env')

SUPABASE_URL = os.environ.get('SUPABASE_URL', '').strip()
SUPABASE_KEY = os.environ.get('SUPABASE_KEY', '').strip()

from supabase import create_client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Tables:")
try:
    res = supabase.table('chatbot_synced_reports').select('id').limit(1).execute()
    print("chatbot_synced_reports works")
except Exception as e:
    print("chatbot_synced_reports failed:", e)
