import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

np.random.seed(1)
w1 = np.random.uniform(-1, 1, (2, 2))
b1 = np.zeros((1, 2))
w2 = np.random.uniform(-1, 1, (2, 1))
b2 = np.zeros((1, 1))
lr = 1.0

for _ in range(20000):
    hidden = sigmoid(X @ w1 + b1)
    output = sigmoid(hidden @ w2 + b2)

    error = output - y
    output_delta = error * output * (1 - output)
    hidden_delta = (output_delta @ w2.T) * hidden * (1 - hidden)

    w2 -= lr * (hidden.T @ output_delta)
    b2 -= lr * np.sum(output_delta, axis=0, keepdims=True)
    w1 -= lr * (X.T @ hidden_delta)
    b1 -= lr * np.sum(hidden_delta, axis=0, keepdims=True)

predicted = (output >= 0.5).astype(int)

print("XOR Perceptron Network")
print("Input    Actual    Predicted")

for inputs, actual, result in zip(X.astype(int), y.astype(int), predicted):
    print(inputs, "    ", actual[0], "        ", result[0])
