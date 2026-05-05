# =========================
# 1. Import Libraries
# =========================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# =========================
# 2. Load Dataset
# =========================
df = pd.read_csv('Mall_Customers.csv')

# View first rows
print(df.head())

# =========================
# 3. Select Features (Income & Spending Score)
# =========================
X = df.iloc[:, [3, 4]].values

# =========================
# 4. Elbow Method (Find Optimal Clusters)
# =========================
wcss_list = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss_list.append(kmeans.inertia_)

# Plot Elbow Graph
plt.plot(range(1, 11), wcss_list)
plt.title('Elbow Method Graph')
plt.xlabel('Number of clusters (K)')
plt.ylabel('WCSS')
plt.show()

# =========================
# 5. Feature Scaling
# =========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================
# 6. Apply K-Means
# =========================
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(X_scaled)

# =========================
# 7. Visualize Clusters
# =========================
plt.scatter(X[y_predict == 0, 0], X[y_predict == 0, 1],
            s=100, c='blue', label='Cluster 1')

plt.scatter(X[y_predict == 1, 0], X[y_predict == 1, 1],
            s=100, c='green', label='Cluster 2')

plt.scatter(X[y_predict == 2, 0], X[y_predict == 2, 1],
            s=100, c='red', label='Cluster 3')

plt.scatter(X[y_predict == 3, 0], X[y_predict == 3, 1],
            s=100, c='black', label='Cluster 4')

plt.scatter(X[y_predict == 4, 0], X[y_predict == 4, 1],
            s=100, c='purple', label='Cluster 5')

# =========================
# 8. Plot Centroids
# =========================
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s=300, c='yellow', label='Centroids')

# =========================
# 9. Final Graph Settings
# =========================
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()