import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

df.to_csv('output.csv', index=False)