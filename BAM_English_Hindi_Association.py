import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
pairs = [
    ("dog", "kutta"),
    ("cat", "billi"),
    ("sun", "suraj"),
    ("moon", "chand"),
    ("tree", "ped"),
    ("book", "kitab"),
    ("water", "paani"),
    ("star", "tara")
]

EN_LEN = 5
HI_LEN = 6
A = 26

def encode(word, length):
    vector = np.zeros(length * A, dtype=int)

    for position, character in enumerate(word[:length]):
        vector[position * A + ord(character) - 97] = 1

    return vector

def decode(vector):
    word = ""

    for index in range(0, len(vector), A):
        block = vector[index:index + A]
        word += chr(97 + int(np.argmax(block))) if block.max() > 0 else ""

    return word

def winner_take_all(score):
    output = np.zeros(len(score), dtype=int)
    strongest = score.max()

    for index in range(0, len(score), A):
        block = score[index:index + A]

        if block.max() > 0 and block.max() >= 0.5 * strongest:
            output[index + int(np.argmax(block))] = 1

    return output

X = np.array([encode(english, EN_LEN) for english, _ in pairs])
Y = np.array([encode(hindi, HI_LEN) for _, hindi in pairs])

print("English layer:", X.shape[1], "neurons; Hindi layer:", Y.shape[1], "neurons")
print("Stored pairs:", len(pairs))

weights = X.T @ Y

def bam_recall(x=None, y=None, iterations=10):
    if x is not None:
        y = winner_take_all(x @ weights)
    else:
        x = winner_take_all(y @ weights.T)

    for _ in range(iterations):
        next_x = winner_take_all(y @ weights.T)
        next_y = winner_take_all(next_x @ weights)

        if np.array_equal(next_x, x) and np.array_equal(next_y, y):
            break

        x, y = next_x, next_y

    return x, y

print("\nForward recall (English -> Hindi):")
forward_correct = 0

for english, hindi in pairs:
    result = decode(bam_recall(x=encode(english, EN_LEN))[1])
    forward_correct += result == hindi
    print(f"{english:6s} -> {result:6s} (expected {hindi})")

print("\nReverse recall (Hindi -> English):")
reverse_correct = 0

for english, hindi in pairs:
    result = decode(bam_recall(y=encode(hindi, HI_LEN))[0])
    reverse_correct += result == english
    print(f"{hindi:6s} -> {result:6s} (expected {english})")

print(f"\nForward accuracy: {forward_correct}/{len(pairs)}   Reverse accuracy: {reverse_correct}/{len(pairs)}")

print("\nSimilar-sounding / misspelt English words (forward):")
for word in ["cot", "dot", "sin", "moan", "boot", "wader"]:
    print(f"{word:6s} -> {decode(bam_recall(x=encode(word, EN_LEN))[1])}")

print("\nSimilar-sounding / alternate Hindi spellings (reverse):")
for word in ["kutti", "billa", "surya", "chaand", "pad", "kitaab"]:
    print(f"{word:6s} -> {decode(bam_recall(y=encode(word, HI_LEN))[0])}")

levels = [0, 1, 2, 4, 6, 8, 10, 12]
trials = 100
forward_accuracy = []
reverse_accuracy = []

print("\nBits flipped in input -> recall accuracy (forward / reverse)")

for flips in levels:
    forward_ok = 0
    reverse_ok = 0

    for (english, hindi), english_vector, hindi_vector in zip(pairs, X, Y):
        for _ in range(trials):
            noisy_english = english_vector.copy()
            indices = rng.choice(len(noisy_english), flips, replace=False)
            noisy_english[indices] = 1 - noisy_english[indices]
            forward_ok += decode(bam_recall(x=noisy_english)[1]) == hindi

            noisy_hindi = hindi_vector.copy()
            indices = rng.choice(len(noisy_hindi), flips, replace=False)
            noisy_hindi[indices] = 1 - noisy_hindi[indices]
            reverse_ok += decode(bam_recall(y=noisy_hindi)[0]) == english

    count = trials * len(pairs)
    forward_accuracy.append(100 * forward_ok / count)
    reverse_accuracy.append(100 * reverse_ok / count)
    print(f"{flips:2d} -> {forward_accuracy[-1]:5.1f}% / {reverse_accuracy[-1]:5.1f}%")

plt.figure(figsize=(6.8, 4.2))
plt.plot(levels, forward_accuracy, marker="o", label="English -> Hindi")
plt.plot(levels, reverse_accuracy, marker="s", label="Hindi -> English")
plt.grid(True)
plt.xlabel("Number of flipped input bits")
plt.ylabel("Recall accuracy (%)")
plt.title("BAM Robustness to Noise")
plt.ylim(-3, 105)
plt.legend()
plt.tight_layout()
plt.savefig("bam_robustness.png", dpi=130)
plt.close()

plt.figure(figsize=(7.4, 3.6))
plt.imshow(weights, cmap="viridis", aspect="auto")
plt.colorbar(label="weight")
plt.xlabel("Hindi neurons (156)")
plt.ylabel("English neurons (130)")
plt.title("BAM Weight Matrix")
plt.tight_layout()
plt.savefig("bam_weight_matrix.png", dpi=130)
plt.close()
