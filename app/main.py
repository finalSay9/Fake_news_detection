from fastapi import FastAPI
from app import schemas
from app.datascience import predict


app = FastAPI() 

@app.get('/')
def read_root():
    return {"message": "Welcome to the Data Science API"}

app.include_router(predict.router)
def data():
    return {'msg': 'hello data science'}


@app.post('/create_user', response_model=schemas.UserResponce)
def creating_user(user: schemas.CreateUser):
    return user
