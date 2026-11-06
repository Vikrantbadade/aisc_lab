import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
n = 500

temperature = np.random.uniform(15, 40, n)
humidity = np.random.uniform(20, 90, n)
occupancy = np.random.randint(0, 6, n)
appliances = np.random.uniform(0.5, 8, n)
hour = np.random.uniform(0, 23, n)

energy = (
    0.08 * temperature
    + 0.025 * humidity
    + 0.35 * occupancy
    + 0.7 * appliances
    + 0.12 * np.maximum(0, 1 - np.abs(hour - 19) / 8)
    + np.random.normal(0, 0.15, n)
)

X = np.column_stack((temperature, humidity, occupancy, appliances, hour))
y = energy

indices = np.random.permutation(n)
train_size = int(0.8 * n)
train_idx = indices[:train_size]
test_idx = indices[train_size:]

X_train = X[train_idx]
X_test = X[test_idx]
y_train = y[train_idx]
y_test = y[test_idx]

minimum = X_train.min(axis=0)
maximum = X_train.max(axis=0)
scale = maximum - minimum
scale[scale == 0] = 1

X_train = (X_train - minimum) / scale
X_test = (X_test - minimum) / scale

n_inputs = X_train.shape[1]
n_mfs = 2
n_rules = n_mfs ** n_inputs

centers = np.zeros((n_inputs, n_mfs))
widths = np.ones((n_inputs, n_mfs)) * 0.3

for feature in range(n_inputs):
    centers[feature] = [0.25, 0.75]

def membership_values(data):
    values = np.empty((len(data), n_inputs, n_mfs))

    for feature in range(n_inputs):
        for mf in range(n_mfs):
            values[:, feature, mf] = np.exp(
                -((data[:, feature] - centers[feature, mf]) ** 2)
                / (2 * widths[feature, mf] ** 2)
            )

    return values

def rule_strengths(data):
    memberships = membership_values(data)
    strengths = np.ones((len(data), n_rules))

    for rule in range(n_rules):
        choices = [(rule >> bit) & 1 for bit in range(n_inputs)]

        for feature, choice in enumerate(choices):
            strengths[:, rule] *= memberships[:, feature, choice]

    return strengths

def design_matrix(data):
    strengths = rule_strengths(data)
    normalized = strengths / (strengths.sum(axis=1, keepdims=True) + 1e-12)
    return np.concatenate([normalized * data[:, feature:feature + 1] for feature in range(n_inputs)] +
                          [normalized], axis=1)

consequents = np.zeros((n_rules, n_inputs + 1))

for epoch in range(40):
    matrix = design_matrix(X_train)
    consequents = np.linalg.lstsq(matrix, y_train, rcond=None)[0].reshape(n_inputs + 1, n_rules).T

    prediction = matrix @ consequents.T.reshape(-1)
    error = prediction - y_train
    rate = 0.002

    for feature in range(n_inputs):
        for mf in range(n_mfs):
            old_center = centers[feature, mf]
            centers[feature, mf] = old_center + rate
            shifted = design_matrix(X_train) @ consequents.T.reshape(-1)
            centers[feature, mf] = old_center - rate
            shifted_back = design_matrix(X_train) @ consequents.T.reshape(-1)
            gradient = np.mean((shifted - shifted_back) * error) / (2 * rate)
            centers[feature, mf] -= 0.0005 * gradient

def predict(data):
    matrix = design_matrix(data)
    flat = consequents.T.reshape(-1)
    return matrix @ flat

predicted = predict(X_test)
rmse = np.sqrt(np.mean((y_test - predicted) ** 2))
mae = np.mean(np.abs(y_test - predicted))
ss_res = np.sum((y_test - predicted) ** 2)
ss_total = np.sum((y_test - np.mean(y_test)) ** 2)
r2 = 1 - ss_res / ss_total

print("ANFIS Household Energy Consumption")
print("Test RMSE:", round(rmse, 3))
print("Test MAE:", round(mae, 3))
print("Test R2:", round(r2, 3))

plt.figure(figsize=(7, 5))
plt.scatter(y_test, predicted, alpha=0.7)
plt.xlabel("Actual Energy Consumption (kWh)")
plt.ylabel("Predicted Energy Consumption (kWh)")
plt.title("ANFIS: Actual vs Predicted")
plt.grid(True)
plt.show()

feature_names = ["Temperature", "Humidity", "Occupancy", "Appliances", "HourOfDay"]

for feature, name in enumerate(feature_names):
    values = np.linspace(0, 1, 100)
    plt.figure(figsize=(6, 4))

    for mf in range(n_mfs):
        curve = np.exp(
            -((values - centers[feature, mf]) ** 2)
            / (2 * widths[feature, mf] ** 2)
        )
        plt.plot(values, curve, label=f"MF {mf + 1}")

    plt.title(name + " Membership Functions")
    plt.xlabel("Normalized Input")
    plt.ylabel("Membership")
    plt.legend()
    plt.grid(True)
    plt.show()
