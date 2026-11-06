import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

digits = load_digits()
X = digits.data
y = digits.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

n_features = X.shape[1]
n_prototypes = 3
prototypes = {}
proto_labels = {}

np.random.seed(42)

for c in np.unique(y_train):
    class_mean = np.mean(X_train[y_train == c], axis=0)
    for p in range(n_prototypes):
        prototypes[(c, p)] = class_mean + 0.01 * np.random.randn(n_features)
        proto_labels[(c, p)] = c

learning_rate = 0.01
epochs = 50

for epoch in range(epochs):
    for xi, yi in zip(X_train, y_train):
        distances = {
            key: np.linalg.norm(xi - weight)
            for key, weight in prototypes.items()
        }
        winner = min(distances, key=distances.get)

        if proto_labels[winner] == yi:
            prototypes[winner] += learning_rate * (xi - prototypes[winner])
        else:
            prototypes[winner] -= learning_rate * (xi - prototypes[winner])

predictions = []

for xi in X_test:
    distances = {
        key: np.linalg.norm(xi - weight)
        for key, weight in prototypes.items()
    }
    winner = min(distances, key=distances.get)
    predictions.append(proto_labels[winner])

accuracy = accuracy_score(y_test, predictions)
print("LVQ Digit Classification")
print("Test Accuracy:", round(accuracy * 100, 2), "%")
