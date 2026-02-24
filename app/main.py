from fastapi import FastAPI
from app import schemas


app = FastAPI() 

@app.get('/')
def data():
    return {'msg': 'hello data science'}


@app.post('/create_user', response_model=schemas.UserResponce)
def creating_user(user: schemas.CreateUser):
    return user
