import numpy as np
import matplotlib.pyplot as plt

noise = np.linspace(0, 100, 200)
low_noise = np.exp(-((noise - 20) ** 2) / (2 * 10 ** 2))
high_noise = np.exp(-((noise - 80) ** 2) / (2 * 10 ** 2))

algebraic_sum = low_noise + high_noise - low_noise * high_noise
algebraic_product = low_noise * high_noise
bounded_sum = np.minimum(low_noise + high_noise, 1)
bounded_difference = np.maximum(low_noise - high_noise, 0)

plt.figure(figsize=(8, 5))
plt.plot(noise, low_noise, label="Low Noise")
plt.plot(noise, high_noise, label="High Noise")
plt.xlabel("Noise Level (dB)")
plt.ylabel("Membership Value")
plt.title("Fuzzy Sets: Low vs High Noise")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(9, 5))
plt.plot(noise, algebraic_sum, label="Algebraic Sum")
plt.plot(noise, algebraic_product, label="Algebraic Product")
plt.plot(noise, bounded_sum, label="Bounded Sum")
plt.plot(noise, bounded_difference, label="Bounded Difference")
plt.xlabel("Noise Level (dB)")
plt.ylabel("Membership Value")
plt.title("Fuzzy Operations")
plt.legend()
plt.grid(True)
plt.show()

aqi = np.array([0, 50, 100, 150, 200, 250, 300, 400], dtype=float)

def triangular(x, a, b, c):
    left = (x - a) / (b - a) if b != a else np.zeros_like(x)
    right = (c - x) / (c - b) if c != b else np.zeros_like(x)
    return np.maximum(0, np.minimum(left, right))

good = np.maximum(0, np.minimum(1, (100 - aqi) / 100))
moderate = triangular(aqi, 50, 125, 200)
poor = triangular(aqi, 150, 250, 350)
severe = np.maximum(0, np.minimum(1, (aqi - 250) / 150))

A = np.array([good, moderate, poor, severe])

health = np.array([0, 1, 2], dtype=float)
healthy = np.array([1.0, 0.3, 0.0])
mild = np.array([0.2, 1.0, 0.3])
serious = np.array([0.0, 0.3, 1.0])
B = np.array([healthy, mild, serious])

category_to_health = np.array([
    [1.0, 0.2, 0.0],
    [0.4, 1.0, 0.2],
    [0.1, 0.7, 0.8],
    [0.0, 0.2, 1.0]
])

relation = np.zeros((len(aqi), 3))

for point in range(len(aqi)):
    for effect in range(3):
        relation[point, effect] = np.max(
            np.minimum(A[:, point], category_to_health[:, effect])
        )

aqi_input_profile = np.exp(-((aqi - 120) ** 2) / (2 * 35 ** 2))

max_min = np.zeros(3)
max_product = np.zeros(3)

for effect in range(3):
    max_min[effect] = np.max(np.minimum(aqi_input_profile, relation[:, effect]))
    max_product[effect] = np.max(aqi_input_profile * relation[:, effect])

print("AQI Fuzzy Sets")
print("AQI values:", aqi.astype(int))
print("Good:", np.round(good, 2))
print("Moderate:", np.round(moderate, 2))
print("Poor:", np.round(poor, 2))
print("Severe:", np.round(severe, 2))

print("\nFuzzy Relation (AQI samples x Health effects)")
print(np.round(relation, 2))
print("\nMax-Min composition [Healthy, Mild, Serious]:")
print(np.round(max_min, 2))
print("\nMax-Product composition [Healthy, Mild, Serious]:")
print(np.round(max_product, 2))

plt.figure(figsize=(9, 5))
for label, values in zip(["Good", "Moderate", "Poor", "Severe"], A):
    plt.plot(aqi, values, marker="o", label=label)
plt.xlabel("Air Quality Index (AQI)")
plt.ylabel("Membership Value")
plt.title("Fuzzy Sets for AQI Categories")
plt.legend()
plt.grid(True)
plt.show()
