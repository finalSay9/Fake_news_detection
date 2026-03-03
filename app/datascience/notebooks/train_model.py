import numpy as np
import pandas as pd
from fastapi import APIRouter
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "house.csv")



data = pd.read_csv(file_path)
# df["Month"] = pd.to_datetime(df["Month"]).dt.month
# df = pd.get_dummies(df, columns=["District"])
# df.describe()
# df.info()
hello = data['District'].value_counts(normalize=True)


df = pd.DataFrame({
    'Product': ['iphone','samsung','oneplus','xiaomi','techno','iphone'],
    'Price': [999,899,699,499,299,999]

})

print(hello)





