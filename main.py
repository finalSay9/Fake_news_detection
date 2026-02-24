from fastapi import FastAPI


app = FastAPI() 

@app.get('/')
def data():
    return {'msg': 'hello data science'}