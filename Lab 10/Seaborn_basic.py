import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


data = pd.DataFrame({'x': [1,2,3,4,5,6], 'y': [2,4,6,8,10,12]})
data2 = pd.DataFrame({'x': [1,2,3,4,5,6], 'y': [1,4,9,16,25,36]})

sns.scatterplot(x='x', y='y', data=data)
sns.scatterplot(x='x', y='y', data=data2)

sns.regplot(x='x', y='y', data=data)
sns.regplot(x='x', y='y', data=data2)

plt.title("ScatterPlot")
plt.show()