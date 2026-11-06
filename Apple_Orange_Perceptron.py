import numpy as np

X = np.array([
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
], dtype=float)

y = np.array([1, 1, 1, 1, 0, 0, 0, 0])

weights = np.zeros(3)
bias = 0.0
learning_rate = 0.1

for _ in range(100):
    errors = 0

    for inputs, target in zip(X, y):
        output = 1 if np.dot(inputs, weights) + bias >= 1.5 else 0
        update = learning_rate * (target - output)
        weights += update * inputs
        bias += update
        errors += int(update != 0)

    if errors == 0:
        break

def predict(inputs):
    value = np.dot(inputs, weights) + bias
    return 1 if value >= 1.5 else 0

test_data = np.array([
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 0]
])

print("Fruit Classification")
print("Shape Texture Weight Prediction")

for inputs in test_data:
    result = predict(inputs)
    fruit = "Apple" if result == 1 else "Orange"
    print(*inputs.astype(int), fruit)
