# Distinguishing Apples and Oranges Using a Perceptron

## Aim
To classify fruits as Apple (`1`) or Orange (`0`) using a simple perceptron-based neural network with shape, texture and weight as input features.

## Theory
A perceptron is a basic neural network model used for binary classification. It receives input features, calculates their weighted sum, adds a bias and applies a threshold activation function to produce a class.

The program uses three input neurons and one output neuron.

### Input Features

| Feature | Value 1 | Value 0 |
|---|---|---|
| Shape | Round | Elliptical |
| Texture | Smooth | Rough |
| Weight | Heavy | Light |

### Output Classes

| Output | Fruit |
|---|---|
| 1 | Apple |
| 0 | Orange |

### Training
The perceptron is trained using labeled fruit data through supervised learning. During training, the predicted output is compared with the actual label. Weights and bias are updated when the prediction is incorrect.

After training, unseen fruit feature combinations are supplied to the model. The model predicts whether each fruit is an Apple or an Orange.

The sample training data in the program assigns Apple to feature combinations with at least two values equal to `1`, and Orange to combinations with fewer than two values equal to `1`. This makes the sample dataset linearly separable so that a single perceptron can learn it.

## Result
The perceptron is trained using the three fruit features and tested with unseen feature combinations. It predicts each test fruit as Apple (`1`) or Orange (`0`).
