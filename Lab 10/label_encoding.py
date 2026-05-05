from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("data.csv")
#Converts categories into numbers (e.g., male → 0, female → 1).
le = LabelEncoder()
print(df['gender'].head())
df['gender'] = le.fit_transform(df['gender'])
print(df['gender'].head())

#Creates separate binary columns for each category.
df = pd.get_dummies(df, columns=['embarked'], drop_first=True)
print(df.head)