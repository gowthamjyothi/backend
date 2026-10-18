from fastapi import FastAPI,Form
from db import supabase

app = FastAPI()

@app.post("/")
def from_data(username : str = Form() ,  passw : str = Form(),phono : int = Form(),interest : str =Form()):
    data ={
        "name" : username,
        "password" : passw,
        "phno" : phono,
        "interest" : interest
    }
    response = supabase.table("users").insert(data).execute()
    return response
