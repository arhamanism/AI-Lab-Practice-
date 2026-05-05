from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

X = df[['age', 'fare']] = df[['age', 'fare']].fillna(df[['age', 'fare']].mean())
y = df['survived']

X = pd.DataFrame(X)
y = pd.Series(y)

kf = KFold(n_splits=5, shuffle=True, random_state=42)

model = LogisticRegression()

accuracy_scores = []

for train_index, test_index in kf.split(X):
        X_train ,  x_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        model.fit(X_train, y_train)

        y_pred = model.predict(x_test)
        acc = accuracy_score(y_pred, y_test)
        accuracy_scores.append(acc)

print("Model accuracy with K-fold split: ", np.mean(accuracy_scores))