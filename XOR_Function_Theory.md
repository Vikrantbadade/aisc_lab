# XOR Function Using a Perceptron-Based Neural Network

## Aim
To implement the XOR function using a perceptron-based neural network in Python.

## Theory
The XOR (Exclusive OR) function gives output `1` when the two input values are different and `0` when they are the same.

### Truth Table

| Input 1 | Input 2 | XOR Output |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

A single-layer perceptron cannot learn XOR because its data is not linearly separable. A network with a hidden layer is required to learn the non-linear decision boundary.

The program uses a neural network with two input neurons, two hidden neurons and one output neuron. The sigmoid activation function converts values into the range 0 to 1. During training, backpropagation calculates the error and updates weights and biases.

The predicted output is converted to `0` or `1` using a threshold of `0.5`.

## Result
The perceptron-based neural network is trained on the XOR truth table and produces the expected output for all four input combinations.
