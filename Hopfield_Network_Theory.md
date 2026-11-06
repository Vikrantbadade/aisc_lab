# Hopfield Network for Handwritten Digit Recognition

## Aim
To design and implement a Hopfield Network that stores binary representations of handwritten digits, reconstructs the original digit from noisy or partial versions, and measures recall accuracy.

## Theory
A Hopfield network is a recurrent, fully connected, auto-associative memory with binary threshold neurons (`+1` and `-1`). Stored patterns become stable states of the network. A noisy or incomplete input can settle into a stored pattern.

### Training: Hebbian Rule
The Hebbian weight matrix is:

`W = (1/N) Σ p(p)ᵀ p(p)`

The diagonal elements are set to zero to prevent self-connections.

### Recall
Neurons are updated one at a time in random order (asynchronous updating):

`xᵢ = +1 if Σⱼ wᵢⱼxⱼ ≥ 0, otherwise −1`

The network energy does not increase during asynchronous updates, so the network converges to a stable state.

### Dataset and Pattern Preparation
The practical uses the 8×8 handwritten digits dataset bundled with scikit-learn because the 28×28 MNIST files could not be downloaded in the original environment. The average image for each selected digit is thresholded to `+1` for stroke and `−1` for background, then flattened into a 64-neuron pattern. The selected digits are 0, 3, 6 and 9.

Noise is introduced by flipping random pixels. Recall accuracy is the percentage of noisy inputs that return exactly to the original stored pattern.

### Pseudo-Inverse Rule
The practical also tests the pseudo-inverse learning rule:

`W = Pᵀ(PPᵀ)⁻¹P`

The pseudo-inverse rule reduces cross-talk between stored patterns. The practical compares it with the plain Hebbian rule because handwritten digit patterns overlap strongly.

## Experiments
1. Store digits 0 and 3 using the Hebbian rule.
2. Store digits 0, 3, 6 and 9 using the Hebbian rule.
3. Store the same four digits using the pseudo-inverse rule.
4. Measure recall accuracy for 0, 2, 4, 6, 8, 10, 12, 16 and 20 flipped pixels.
5. Test partial input by hiding the bottom four rows.
6. Test binarized real handwritten samples and plot stored patterns, noisy/recalled examples and recall accuracy.

## Result
The supplied practical reports that the two-digit Hebbian network stored both patterns stably and achieved 97.5% recall at 20 flipped pixels. For four digits, plain Hebbian learning failed because the patterns overlapped. The pseudo-inverse rule made all four patterns stable, achieved 100% recall up to 8 flipped pixels, and 72.0% at 20 flips. It reconstructed all four half-hidden digits and recalled 636 of 722 real handwritten samples correctly (88.1%).

## Requirements
Install the required libraries using:

`pip install numpy matplotlib scikit-learn`
