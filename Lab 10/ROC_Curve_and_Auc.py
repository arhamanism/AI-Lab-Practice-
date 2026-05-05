from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# -----------------------------
# 1. Load dataset
# -----------------------------
df = sns.load_dataset('titanic')

# Select features and target
X = df[['age', 'fare']]
y = df['survived']

# Handle missing values
X = X.fillna(X.mean())

# -----------------------------
# 2. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 3. Train Decision Tree model
# -----------------------------
DT = DecisionTreeClassifier(random_state=42)
DT.fit(X_train, y_train)

# -----------------------------
# 4. Get probability predictions
# -----------------------------
probabilities = DT.predict_proba(X_test)[:, 1]

# -----------------------------
# 5. Compute ROC curve
# -----------------------------
fpr, tpr, thresholds = roc_curve(y_test, probabilities)

# -----------------------------
# 6. Compute AUC score
# -----------------------------
roc_auc = roc_auc_score(y_test, probabilities)

# -----------------------------
# 7. Plot ROC curve
# -----------------------------
plt.figure(figsize=(8, 6))

# ROC curve
plt.plot(fpr, tpr, color='blue', lw=2,
         label=f'ROC Curve (AUC = {roc_auc:.2f})')

# Area under curve
plt.fill_between(fpr, tpr, color='skyblue', alpha=0.4)

# Random classifier line
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')

# Labels and formatting
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve with AUC Area')
plt.legend(loc='lower right')

plt.show()