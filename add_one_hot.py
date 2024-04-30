import pandas as pd

data = pd.read_csv('datasets/data.csv')

data = pd.get_dummies(data, columns=['Sex'])

data.to_csv('datasets/data.csv', index=False)