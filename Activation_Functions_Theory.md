# Activation and Transfer Functions

## Aim
To understand and implement various transfer/activation functions for a given problem statement.

## Theory
In Artificial Neural Networks (ANNs), neurons compute a weighted sum of their inputs, add a bias, and then apply a transfer or activation function to determine the final output.

Activation or transfer functions are mathematical equations that determine the output of a neural network model. They map an input signal to an output signal, often introducing non-linearity into the network. This enables neural networks to learn and model complex patterns. Without non-linear activation functions, a neural network would behave like a linear regression model, regardless of the number of layers.

## Functions

1. **Symmetric Hard Limit:** Returns `1` when the input is greater than or equal to the threshold and `-1` otherwise. The threshold used in the practical is `2`.
2. **Binary Step:** Returns `1` when the input is greater than or equal to `0`, and `0` otherwise.
3. **Bipolar Step:** Returns `1` when the input is greater than or equal to `0`, and `-1` otherwise.
4. **Saturating Linear:** Returns `-1` below `-1`, the input value between `-1` and `1`, and `1` above `1`.
5. **Hyperbolic Tangent Sigmoid (tansig):** Uses the hyperbolic tangent function, `tanh(x)`, and produces values between `-1` and `1`.
6. **Log-Sigmoid:** Uses `1 / (1 + exp(-x))` and produces values between `0` and `1`.

## Result
The six activation/transfer functions are implemented and their input-output curves are plotted.
