import numpy as np
import matplotlib.pyplot as plt

def trimf(x, a, b, c):
    left = np.zeros_like(x, dtype=float) if a == b else (x - a) / (b - a)
    right = np.zeros_like(x, dtype=float) if b == c else (c - x) / (c - b)
    return np.maximum(0, np.minimum(left, right))

def trapmf(x, a, b, c, d):
    rising = np.ones_like(x, dtype=float) if a == b else (x - a) / (b - a)
    falling = np.ones_like(x, dtype=float) if c == d else (d - x) / (d - c)
    return np.maximum(0, np.minimum(1, np.minimum(rising, falling)))

density = np.arange(0, 51, 1)
waiting = np.arange(0, 121, 1)
green = np.arange(10, 91, 1)

density_mf = {
    "low": trapmf(density, 0, 0, 8, 15),
    "medium": trimf(density, 10, 20, 30),
    "high": trapmf(density, 25, 35, 50, 50)
}

waiting_mf = {
    "short": trapmf(waiting, 0, 0, 15, 30),
    "moderate": trimf(waiting, 20, 50, 80),
    "long": trapmf(waiting, 70, 90, 120, 120)
}

green_mf = {
    "short": trapmf(green, 10, 10, 20, 30),
    "medium": trimf(green, 30, 45, 60),
    "long": trapmf(green, 60, 75, 90, 90)
}

rules = [
    ("low", "short", "short"),
    ("low", "moderate", "short"),
    ("low", "long", "medium"),
    ("medium", "short", "medium"),
    ("medium", "moderate", "medium"),
    ("medium", "long", "long"),
    ("high", "short", "medium"),
    ("high", "moderate", "long"),
    ("high", "long", "long")
]

def controller(vehicle_count, wait_seconds):
    if not 0 <= vehicle_count <= 50:
        raise ValueError("Traffic density must be between 0 and 50 vehicles.")
    if not 0 <= wait_seconds <= 120:
        raise ValueError("Waiting time must be between 0 and 120 seconds.")

    density_degree = {
        name: np.interp(vehicle_count, density, values)
        for name, values in density_mf.items()
    }

    waiting_degree = {
        name: np.interp(wait_seconds, waiting, values)
        for name, values in waiting_mf.items()
    }

    aggregated = np.zeros_like(green, dtype=float)

    for density_label, waiting_label, output_label in rules:
        strength = min(
            density_degree[density_label],
            waiting_degree[waiting_label]
        )
        clipped = np.minimum(strength, green_mf[output_label])
        aggregated = np.maximum(aggregated, clipped)

    if np.sum(aggregated) == 0:
        return 45.0

    duration = np.sum(green * aggregated) / np.sum(aggregated)
    return duration

test_cases = [
    (5, 10),
    (20, 50),
    (40, 100),
    (35, 100)
]

print("Fuzzy Traffic Light Controller")
print("Density  Waiting  Green Duration")

for vehicles, wait in test_cases:
    duration = controller(vehicles, wait)
    print(f"{vehicles:7d}  {wait:7d}  {duration:14.2f} seconds")

plt.figure(figsize=(8, 4))
for name, values in density_mf.items():
    plt.plot(density, values, label=name)
plt.title("Traffic Density Membership Functions")
plt.xlabel("Vehicles per minute")
plt.ylabel("Membership")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
for name, values in waiting_mf.items():
    plt.plot(waiting, values, label=name)
plt.title("Waiting Time Membership Functions")
plt.xlabel("Waiting time (seconds)")
plt.ylabel("Membership")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
for name, values in green_mf.items():
    plt.plot(green, values, label=name)
plt.title("Green Light Duration Membership Functions")
plt.xlabel("Green duration (seconds)")
plt.ylabel("Membership")
plt.legend()
plt.grid(True)
plt.show()

density_values = np.arange(0, 51, 2)
waiting_values = np.arange(0, 121, 5)
surface = np.zeros((len(waiting_values), len(density_values)))

for i, wait in enumerate(waiting_values):
    for j, vehicles in enumerate(density_values):
        surface[i, j] = controller(int(vehicles), int(wait))

plt.figure(figsize=(8, 5))
plt.contourf(density_values, waiting_values, surface, levels=15)
plt.colorbar(label="Green duration (seconds)")
plt.xlabel("Traffic density (vehicles/min)")
plt.ylabel("Waiting time (seconds)")
plt.title("Fuzzy Traffic Light Control Surface")
plt.show()
