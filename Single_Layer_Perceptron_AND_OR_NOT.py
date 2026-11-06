import numpy as np
import matplotlib.pyplot as plt

def train_perceptron(X, y, learning_rate=0.1, epochs=100):
    weights = np.zeros(X.shape[1])
    bias = 0.0

    for _ in range(epochs):
        errors = 0
        for inputs, target in zip(X, y):
            output = 1 if np.dot(inputs, weights) + bias >= 0 else 0
            update = learning_rate * (target - output)
            weights += update * inputs
            bias += update
            errors += int(update != 0)
        if errors == 0:
            break

    return weights, bias

def predict(X, weights, bias):
    return np.where(np.dot(X, weights) + bias >= 0, 1, 0)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

gates = {
    "AND": np.array([0, 0, 0, 1]),
    "OR": np.array([0, 1, 1, 1])
}

for name, y in gates.items():
    weights, bias = train_perceptron(X, y)
    predicted = predict(X, weights, bias)

    print(name)
    print("Actual:   ", y.tolist())
    print("Predicted:", predicted.tolist())
    print("Weights:", weights, "Bias:", bias)

    plt.figure(figsize=(5, 4))
    for point, target in zip(X, y):
        plt.scatter(point[0], point[1], marker="o" if target == 0 else "s", s=100)

    x1 = np.linspace(-0.2, 1.2, 100)
    if abs(weights[1]) > 1e-10:
        x2 = -(weights[0] * x1 + bias) / weights[1]
        plt.plot(x1, x2)
    plt.xlim(-0.2, 1.2)
    plt.ylim(-0.2, 1.2)
    plt.xlabel("Input 1")
    plt.ylabel("Input 2")
    plt.title(name + " Decision Boundary")
    plt.grid(True)
    plt.show()

X_not = np.array([[0], [1]])
y_not = np.array([1, 0])
weights, bias = train_perceptron(X_not, y_not)
predicted = predict(X_not, weights, bias)

print("NOT")
print("Actual:   ", y_not.tolist())
print("Predicted:", predicted.tolist())
