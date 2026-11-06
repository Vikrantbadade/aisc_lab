import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

rng = np.random.default_rng(13)
N = 64
data = load_digits()

def template(digit):
    images = data.images[data.target == digit] / 16.0
    average = images.mean(axis=0)
    return np.where(average > 0.4, 1, -1).flatten()

def samples(digit):
    return data.images[data.target == digit] / 16.0

def train(patterns, rule):
    if rule == "hebbian":
        weights = patterns.T @ patterns / N
    else:
        weights = patterns.T @ np.linalg.inv(patterns @ patterns.T) @ patterns
    np.fill_diagonal(weights, 0)
    return weights

def recall(weights, pattern, max_sweeps=20):
    state = pattern.astype(float).copy()

    for _ in range(max_sweeps):
        changed = False

        for index in rng.permutation(N):
            value = 1 if weights[index] @ state >= 0 else -1

            if value != state[index]:
                state[index] = value
                changed = True

        if not changed:
            break

    return state

def identify(patterns, digits, state):
    for index, pattern in enumerate(patterns):
        if np.array_equal(state, pattern):
            return digits[index]
    return None

def accuracy(weights, patterns, flips, trials):
    correct = 0

    for pattern in patterns:
        for _ in range(trials):
            noisy = pattern.copy()
            noisy[rng.choice(N, flips, replace=False)] *= -1
            correct += np.array_equal(recall(weights, noisy), pattern)

    return 100 * correct / (trials * len(patterns))

levels = [0, 2, 4, 6, 8, 10, 12, 16, 20]
trials = 100

def report(title, digits, rule):
    patterns = np.array([template(digit) for digit in digits])
    weights = train(patterns, rule)
    stable = all(np.array_equal(recall(weights, pattern), pattern) for pattern in patterns)

    print(f"\n=== {title}: digits {digits}, rule = {rule} ===")
    print("All stored patterns stable:", stable)

    accuracies = []

    for flips in levels:
        value = accuracy(weights, patterns, flips, trials)
        accuracies.append(value)
        print(f"{flips:2d} flipped pixels ({100 * flips / N:4.1f}%) -> {value:5.1f}% recalled correctly")

    return patterns, weights, accuracies

patterns_a, weights_a, accuracy_a = report("A", [0, 3], "hebbian")
digits_b = [0, 3, 6, 9]
patterns_b, weights_b_hebbian, accuracy_b_hebbian = report("B1", digits_b, "hebbian")
_, weights_b_pinv, accuracy_b_pinv = report("B2", digits_b, "pinv")

print("\nPartial input (bottom half hidden), 4 digits, pseudo-inverse rule:")
correct = 0

for index, pattern in enumerate(patterns_b):
    partial = pattern.astype(float).copy()
    partial[32:] = 0
    result = identify(patterns_b, digits_b, recall(weights_b_pinv, partial))
    correct += result == digits_b[index]
    print(f"digit {digits_b[index]} -> recalled {result}")

print(f"{correct}/{len(patterns_b)} recalled correctly")

print("\nReal handwritten samples (binarised, not the templates), pseudo-inverse:")
total = 0
correct = 0

for digit in digits_b:
    digit_correct = 0

    for image in samples(digit):
        pattern = np.where(image.flatten() > image.mean(), 1, -1)
        digit_correct += identify(patterns_b, digits_b, recall(weights_b_pinv, pattern)) == digit

    total += len(samples(digit))
    correct += digit_correct
    print(f"digit {digit}: {digit_correct}/{len(samples(digit))}")

print(f"overall {correct}/{total} = {100 * correct / total:.1f}%")

fig, axes = plt.subplots(1, 4, figsize=(8, 2.4))
for axis, pattern, digit in zip(axes, patterns_b, digits_b):
    axis.imshow(pattern.reshape(8, 8), cmap="gray_r")
    axis.set_title(f"Stored {digit}")
    axis.axis("off")
plt.tight_layout()
plt.savefig("hopfield_stored_digits.png", dpi=130)
plt.close()

fig, axes = plt.subplots(3, 4, figsize=(8, 6.2))
row_labels = ["Original", "Noisy (8 flips)", "Recalled"]

for column, pattern in enumerate(patterns_b):
    noisy = pattern.copy()
    noisy[rng.choice(N, 8, replace=False)] *= -1
    recovered = recall(weights_b_pinv, noisy)

    for row, image in enumerate([pattern, noisy, recovered]):
        axes[row][column].imshow(image.reshape(8, 8), cmap="gray_r")
        axes[row][column].set_xticks([])
        axes[row][column].set_yticks([])
        if column == 0:
            axes[row][column].set_ylabel(row_labels[row], fontsize=9)

plt.tight_layout()
plt.savefig("hopfield_recall_examples.png", dpi=130)
plt.close()

plt.figure(figsize=(6.8, 4.2))
plt.plot(levels, accuracy_a, marker="o", label="Hebbian, digits 0 and 3")
plt.plot(levels, accuracy_b_hebbian, marker="s", label="Hebbian, digits 0, 3, 6, 9")
plt.plot(levels, accuracy_b_pinv, marker="^", label="Pseudo-inverse, digits 0, 3, 6, 9")
plt.grid(True)
plt.xlabel("Number of flipped pixels (out of 64)")
plt.ylabel("Recall accuracy (%)")
plt.title("Hopfield Recall Accuracy vs Noise")
plt.ylim(-3, 105)
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig("hopfield_accuracy.png", dpi=130)
plt.close()
