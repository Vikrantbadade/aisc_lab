# Backpropagation Algorithm

## Aim
To calculate the new weights of a neural network using the backpropagation algorithm.

## Theory
Backpropagation is a supervised learning algorithm used to train artificial neural networks. It calculates the error between the predicted output and the target output, propagates this error backward through the network, and updates the weights and biases.

The network in the supplied example contains:
- Two input neurons: `x1` and `x2`
- Two hidden neurons: `z1` and `z2`
- One output neuron: `y`
- Binary sigmoid activation function
- Learning rate: `0.25`

The input pattern is `[0, 1]` and the target output is `1`.

### Sigmoid Activation Function

`f(x) = 1 / (1 + e^(-x))`

The derivative of the sigmoid function is:

`f'(x) = f(x) * (1 - f(x))`

### Steps
1. Initialize the weights and biases with the given values.
2. Perform forward propagation to calculate hidden-layer and output-layer values.
3. Calculate the output error using the target and predicted output.
4. Propagate the error to the hidden layer.
5. Calculate weight changes using the learning rate.
6. Update all weights and biases.

### Initial Weights

| Weight | Initial value |
|---|---:|
| v11 | 0.6 |
| v21 | -0.1 |
| v01 | 0.3 |
| v12 | -0.3 |
| v22 | 0.4 |
| v02 | 0.5 |
| w1 | 0.4 |
| w2 | 0.1 |
| w0 | -0.2 |

## Result
The program performs one forward and backward pass for input `[0, 1]`, target `1`, and learning rate `0.25`. It displays the network output and updated weights.
