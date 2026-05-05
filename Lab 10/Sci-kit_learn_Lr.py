import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1,2,3,4,5]]).reshape(-1, 1)
y = np.array([2,4,6,8,10])

test = np.array([4,3,9]).reshape(-1,1)

model = LinearRegression()
model.fit(X,y)

print(model.predict(X))
print(model.predict(test))
