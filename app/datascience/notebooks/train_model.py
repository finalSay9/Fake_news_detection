import numpy as np
import pandas as pd
from fastapi import APIRouter
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "house.csv")



df = pd.read_csv(file_path)
# df["Month"] = pd.to_datetime(df["Month"]).dt.month
# df = pd.get_dummies(df, columns=["District"])
# df.describe()
# df.info()
# df['District'].value_counts()


data = pd.Dataframe({
    'Month': [1,2,3,4,5,6,7,8,9,10,11,12],
    'District': ['A','B','C','D','E','F','G','H','I','J','K','L'],
    'Price': [100,150,200,250,300,350,400,450,500,550,600,650],
    
})





