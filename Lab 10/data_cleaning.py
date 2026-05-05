import pandas as pd

df = pd.read_csv("data.csv")

#check for missing value
print(df.isnull().sum())
print(df.shape)

#dropping missing value
df_cleaned = df.dropna()
print(df_cleaned.shape)

#Handle missing value
df['age'] = df['age'].fillna(df['age'].mean())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df['deck'] = df['deck'].astype(str).fillna('Unknown')

df = df.dropna()
print(df.shape)
print(df.isnull().sum())