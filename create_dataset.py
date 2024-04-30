import pandas as pd
from catboost.datasets import titanic

df, _ = titanic()

df.to_csv('datasets/data.csv', index=False)