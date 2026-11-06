import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

def symmetric_hard_limit(x, threshold=2):
    return np.where(x >= threshold, 1, -1)

def binary_step(x):
    return np.where(x >= 0, 1, 0)

def bipolar_step(x):
    return np.where(x >= 0, 1, -1)

def saturating_linear(x):
    return np.where(x < -1, -1, np.where(x > 1, 1, x))

def tansig(x):
    return np.tanh(x)

def log_sigmoid(x):
    return 1 / (1 + np.exp(-x))

functions = [
    ("Symmetric Hard Limit Transfer Function", symmetric_hard_limit(x)),
    ("Binary Step Activation Function", binary_step(x)),
    ("Bipolar Step Activation Function", bipolar_step(x)),
    ("Saturating Linear Transfer Function", saturating_linear(x)),
    ("Hyperbolic Tangent Sigmoid (tansig)", tansig(x)),
    ("Log-Sigmoid Transfer Function", log_sigmoid(x))
]

for title, y in functions:
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, linewidth=2)
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
    plt.axvline(0, color="red", linestyle="--", linewidth=0.8)
    plt.title(title)
    plt.xlabel("Input (x)")
    plt.ylabel("Output")
    plt.grid(True)
    plt.show()
