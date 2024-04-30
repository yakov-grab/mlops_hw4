import pandas as pd

data = pd.read_csv('datasets/data.csv')

mean_age = data['Age'].mean()

data['Age'].fillna(mean_age, inplace=True)
data['Age'] = data['Age'].round(2)

data.to_csv('datasets/data.csv', index=False)