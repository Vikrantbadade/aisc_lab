# Single-Layer Perceptron: AND, OR and NOT Gates

## Aim
To design and implement a single-layer perceptron to learn AND, OR and NOT gates using Python.

## Theory
A perceptron is a basic artificial neuron. It calculates a weighted sum of inputs, adds a bias, and applies an activation function to produce an output.

The perceptron learning rule updates weights and bias when the predicted output differs from the target output. A single-layer perceptron can learn linearly separable logic gates such as AND and OR. The NOT gate has one input and can also be implemented using a perceptron.

## Input
For AND and OR, the input combinations are:

`[[0, 0], [0, 1], [1, 0], [1, 1]]`

## Truth Tables

| A | B | AND | OR |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

| A | NOT A |
|---|---|
| 0 | 1 |
| 1 | 0 |

## Decision Boundary
A decision boundary separates input points assigned to different output classes. The practical plots decision boundaries for AND and OR.

## Why a Single-Layer Perceptron Cannot Solve XOR
A single-layer perceptron can represent only a linear decision boundary. The XOR outputs cannot be separated into two classes using one straight line. Therefore, XOR cannot be learned by a single-layer perceptron.

## Result
The single-layer perceptron is implemented for AND, OR and NOT gates. Actual and predicted outputs are displayed, and decision boundary plots are generated for AND and OR.
