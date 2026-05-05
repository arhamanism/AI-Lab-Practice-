import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df[['age', 'fare']].hist(bins=20, figsize=(8,20))
plt.show()

