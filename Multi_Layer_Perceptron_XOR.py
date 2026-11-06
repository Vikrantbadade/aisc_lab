import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

np.random.seed(1)
weights1 = np.random.uniform(-1, 1, (2, 4))
bias1 = np.zeros((1, 4))
weights2 = np.random.uniform(-1, 1, (4, 1))
bias2 = np.zeros((1, 1))
learning_rate = 1.0

for _ in range(20000):
    hidden = sigmoid(X @ weights1 + bias1)
    output = sigmoid(hidden @ weights2 + bias2)

    output_error = output - y
    output_delta = output_error * output * (1 - output)
    hidden_delta = (output_delta @ weights2.T) * hidden * (1 - hidden)

    weights2 -= learning_rate * (hidden.T @ output_delta)
    bias2 -= learning_rate * np.sum(output_delta, axis=0, keepdims=True)
    weights1 -= learning_rate * (X.T @ hidden_delta)
    bias1 -= learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

predicted = (output >= 0.5).astype(int)

print("XOR Truth Table")
print("Input     Actual  Predicted")
for inputs, actual, result in zip(X.astype(int), y.astype(int), predicted):
    print(inputs, "    ", actual[0], "      ", result[0])

xx, yy = np.meshgrid(np.linspace(-0.2, 1.2, 200), np.linspace(-0.2, 1.2, 200))
grid = np.c_[xx.ravel(), yy.ravel()]
hidden_grid = sigmoid(grid @ weights1 + bias1)
output_grid = sigmoid(hidden_grid @ weights2 + bias2).reshape(xx.shape)

plt.figure(figsize=(6, 5))
plt.contourf(xx, yy, output_grid, levels=[0, 0.5, 1], alpha=0.3)
for point, target in zip(X, y):
    plt.scatter(point[0], point[1], s=100, marker="o" if target[0] == 0 else "s")
plt.xlabel("Input 1")
plt.ylabel("Input 2")
plt.title("XOR Decision Boundary")
plt.grid(True)
plt.show()
