# -*- coding: utf-8 -*-
"""DimasArbiArdian_KMeans_Iris.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cuaGjlxRHJfa0Qo3silI5zHj4EuB-hEe
"""

# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris #dataset Iris
from sklearn.cluster import KMeans

# Memuat dataset Iris
iris = load_iris()
X = iris.data

# Menjalankan algoritma K-Means dengan jumlah cluster yang ditentukan
kmeans = KMeans(n_clusters=5) #jumlah cluster
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Memvisualisasikan hasil clustering
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

# Menampilkan pusat cluster (centroid)
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('K-Means Clustering on Iris Dataset')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance
from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer
from yellowbrick.cluster import InterclusterDistance, SilhouetteVisualizer

# Generate some sample data
X, _ = make_blobs(n_samples=100, centers=4, cluster_std=0.60, random_state=0)

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method to determine the optimal number of clusters
model = KMeans()
visualizer = KElbowVisualizer(model, k=(2,10), metric='distortion')
visualizer.fit(X_scaled)
visualizer.show()

# Silhouette Visualizer
visualizer = SilhouetteVisualizer(KMeans(4, random_state=0), colors='yellowbrick')
visualizer.fit(X_scaled)
visualizer.show()

# KMeans clustering with optimal number of clusters
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_scaled)

# Plotting the clusters
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans.labels_, cmap='viridis', s=50, alpha=0.8)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X')
plt.title('Clustering Results')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# Evaluate clustering using Silhouette Score
silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)
print(f'Silhouette Score: {silhouette_avg}')

# Evaluate clustering using Sum of Squared Errors (SSE)
sse = np.sum((X_scaled - kmeans.cluster_centers_[kmeans.labels_]) ** 2)
print(f'SSE: {sse}')

# Evaluate clustering using Davies-Bouldin Index
db_index = davies_bouldin_score(X_scaled, kmeans.labels_)
print(f'Davies-Bouldin Index: {db_index}')

# Evaluate clustering using Calinski-Harabasz Index (Chi)
calinski_harabasz_index = calinski_harabasz_score(X_scaled, kmeans.labels_)
print(f'Calinski-Harabasz Index: {calinski_harabasz_index}')

# Dunn Index
def dunn_index(X, labels):
    min_inter_cluster_distance = np.inf
    max_intra_cluster_diameter = -np.inf
    for i in np.unique(labels):
        cluster_points = X[labels == i]
        max_intra_cluster_diameter = max(max_intra_cluster_diameter, np.max(distance.pdist(cluster_points)))
        for j in np.unique(labels):
            if i != j:
                other_cluster_points = X[labels == j]
                min_inter_cluster_distance = min(min_inter_cluster_distance, np.min(distance.cdist(cluster_points, other_cluster_points)))
    dunn = min_inter_cluster_distance / max_intra_cluster_diameter
    return dunn

dunn = dunn_index(X_scaled, kmeans.labels_)
print(f'Dunn Index: {dunn}')