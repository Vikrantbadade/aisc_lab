import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

data = pd.read_csv("heart_failure_clinical_records_dataset.csv")

labels = data["DEATH_EVENT"].to_numpy()
features = data.drop(columns=["DEATH_EVENT"])
X = StandardScaler().fit_transform(features)

grid_size = 10
n_features = X.shape[1]
learning_rate = 0.5
iterations = 5000

np.random.seed(42)
weights = np.random.rand(grid_size, grid_size, n_features)

for step in range(iterations):
    sample = X[np.random.randint(len(X))]
    distances = np.linalg.norm(weights - sample, axis=2)
    bmu = np.unravel_index(np.argmin(distances), distances.shape)

    radius = max(1, grid_size * (1 - step / iterations) / 2)
    rate = learning_rate * (1 - step / iterations)

    for i in range(grid_size):
        for j in range(grid_size):
            distance = np.sqrt((i - bmu[0]) ** 2 + (j - bmu[1]) ** 2)

            if distance <= radius:
                influence = np.exp(-(distance ** 2) / (2 * radius ** 2))
                weights[i, j] += rate * influence * (sample - weights[i, j])

bmus = []

for sample in X:
    distances = np.linalg.norm(weights - sample, axis=2)
    bmus.append(np.unravel_index(np.argmin(distances), distances.shape))

bmus = np.array(bmus)
cluster_ids = bmus[:, 0] * grid_size + bmus[:, 1]
unique_clusters = np.unique(cluster_ids)

print("SOM Heart Failure Clustering")
print("Number of patients:", len(X))
print("Number of occupied clusters:", len(unique_clusters))

if len(unique_clusters) > 1:
    score = silhouette_score(X, cluster_ids)
    print("Silhouette Score:", round(score, 4))

print("\nCluster-wise patient count and death event rate")
for cluster in unique_clusters:
    mask = cluster_ids == cluster
    print(
        "Cluster", cluster,
        "Patients:", int(np.sum(mask)),
        "Death event rate:", round(float(np.mean(labels[mask])), 3)
    )

plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    bmus[:, 1], bmus[:, 0],
    c=labels, cmap="coolwarm", s=45, edgecolors="black"
)
plt.colorbar(scatter, label="DEATH_EVENT")
plt.title("SOM Patient Clusters")
plt.xlabel("SOM Grid Column")
plt.ylabel("SOM Grid Row")
plt.grid(True)
plt.show()
