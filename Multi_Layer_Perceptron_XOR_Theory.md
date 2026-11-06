# Multi-Layer Perceptron: XOR Gate

## Aim
To design and implement a multi-layer perceptron to learn the XOR gate using Python.

## Theory
A multi-layer perceptron (MLP) is a feedforward artificial neural network containing an input layer, one or more hidden layers, and an output layer. It uses weights, biases and activation functions to learn relationships between inputs and outputs.

The XOR gate produces an output of `1` when its two inputs are different and `0` when they are the same. Its truth table is:

| A | B | XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

A single-layer perceptron cannot learn XOR because the data is not linearly separable. An MLP with a hidden layer can learn the non-linear relationship.

The sigmoid activation function is:

`f(x) = 1 / (1 + exp(-x))`

The network uses forward propagation to calculate outputs and backpropagation to update weights and biases based on the prediction error.

## Deliverables
1. Truth table showing actual and predicted outputs.
2. Decision boundary plot.

## Difference Between AND and XOR
AND is linearly separable, so a single-layer perceptron can learn it. XOR is not linearly separable, so it requires a multi-layer perceptron with a hidden layer.

## Result
A multi-layer perceptron is implemented to learn the XOR gate. The actual and predicted truth-table outputs and the decision boundary are displayed.
