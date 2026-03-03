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


df = pd.DataFrame(np.random.rand(10,10),
                  index=[f'Row{i}' for i in range(10)],
                  columns=[f'Col{j}' for j in range(10)])

data = pd.Series(np.random.rand(10),
                index=[f'Row{i}' for i in range(10)],
                )


result = df.add(data, axis='index')
print(result)





