from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import pandas as pd
import numpy as np



df = sns.load_dataset('titanic')

X = df[['age', 'fare']] = df[['age', 'fare']].fillna(df[['age', 'fare']].mean())
y = df['survived']

X = pd.DataFrame(X)
y = pd.Series(y)

model = LogisticRegression()
loocv = LeaveOneOut()
loo_scores = []

for train_index, test_index in loocv.split(X):
    X_train, x_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    model.fit(X_train, y_train)
    y_pred = model.predict(x_test)

    acc = accuracy_score(y_pred, y_test)
    loo_scores.append(acc)

print(np.mean(loo_scores))