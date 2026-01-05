import os
from dotenv import load_dotenv

from supabase import create_client, Client
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)





def login_BD(email,password):

    response = (
    supabase.table("Usuarios")
    .select("email,password")
    .execute()
    )

    BD =response.data # esto es una lista
    if BD[0]["email"] == email and BD[0]["password"]:
        return True
    else:
        return False