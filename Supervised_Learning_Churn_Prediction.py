import numpy as np

np.random.seed(7)

data_size = 120
tenure = np.random.randint(1, 72, data_size)
monthly_charges = np.random.randint(20, 121, data_size)
support_calls = np.random.randint(0, 8, data_size)
service_count = np.random.randint(1, 6, data_size)

X = np.column_stack((tenure, monthly_charges, support_calls, service_count)).astype(float)
y = ((monthly_charges > 75) & ((tenure < 30) | (support_calls >= 4))).astype(float).reshape(-1, 1)

split = int(0.8 * data_size)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

mean = X_train.mean(axis=0)
std = X_train.std(axis=0)
std[std == 0] = 1

X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

np.random.seed(1)
weights1 = np.random.randn(4, 8) * 0.1
bias1 = np.zeros((1, 8))
weights2 = np.random.randn(8, 1) * 0.1
bias2 = np.zeros((1, 1))
learning_rate = 0.1

for epoch in range(3000):
    hidden = sigmoid(X_train @ weights1 + bias1)
    output = sigmoid(hidden @ weights2 + bias2)

    output_delta = output - y_train
    hidden_delta = (output_delta @ weights2.T) * hidden * (1 - hidden)

    weights2 -= learning_rate * (hidden.T @ output_delta) / len(X_train)
    bias2 -= learning_rate * np.mean(output_delta, axis=0, keepdims=True)
    weights1 -= learning_rate * (X_train.T @ hidden_delta) / len(X_train)
    bias1 -= learning_rate * np.mean(hidden_delta, axis=0, keepdims=True)

test_hidden = sigmoid(X_test @ weights1 + bias1)
test_output = sigmoid(test_hidden @ weights2 + bias2)
predictions = (test_output >= 0.5).astype(int)

actual = y_test.astype(int)
accuracy = np.mean(predictions == actual) * 100

tp = np.sum((predictions == 1) & (actual == 1))
fp = np.sum((predictions == 1) & (actual == 0))
fn = np.sum((predictions == 0) & (actual == 1))

precision = tp / (tp + fp) if tp + fp else 0
recall = tp / (tp + fn) if tp + fn else 0
f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0

print("Customer Churn Prediction")
print("Actual   Predicted")

for a, p in zip(actual.flatten(), predictions.flatten()):
    print(int(a), "       ", int(p))

print("\nAccuracy:", round(accuracy, 2), "%")
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))
print("F1-score:", round(f1, 2))
