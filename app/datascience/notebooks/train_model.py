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
#hello = data['District'].value_counts(normalize=True)




bin_edges =[0,10000000,17000000,20000000,25000000,30000000]
group_prices = ['cheap','affordable','expensive','too expensive','luxury']

df['Price_Category'] = pd.cut(df['House_Price'], bins=bin_edges, labels=group_prices, include_lowest=True)

print(df)





