import numpy as np
import pandas as pd
from fastapi import APIRouter
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "hello.csv")



df = pd.read_csv(file_path)


router = APIRouter(
    prefix='/predict',
    tags = ['predict']
)



@router.get('/read_data')
def read_data():
    return df.to_dict()