# Supervised Learning Using Backpropagation

## Aim
To implement a supervised learning algorithm using a neural network and binary sigmoid activation.

## Theory
Supervised learning trains a model using labeled examples. Each training example contains input features and a known target output. The network predicts an output, compares it with the target, and updates its weights to reduce the error.

The supplied Experiment 5 document describes the following procedure:

1. Prepare and load the dataset.
2. Preprocess the data by handling missing values, scaling numerical features and encoding categorical features where required.
3. Split the dataset into training data (70–80%) and testing data (20–30%).
4. Design a neural network with an input layer matching the number of features, one or more hidden layers, and an output layer.
5. Use a binary sigmoid activation function for binary classification.
6. Train the network using forward propagation, error calculation, backpropagation and gradient descent.
7. Evaluate the model using accuracy, precision, recall and F1-score.

### Binary Sigmoid Function

`f(x) = 1 / (1 + e^(-x))`

The output is between 0 and 1. A threshold such as `0.5` can be used to convert the output into a binary class.

## Practical Implementation
The accompanying Python program demonstrates customer churn classification using a small generated dataset. The input features are tenure, monthly charges, support calls and service count. The target represents whether the customer is predicted to churn.

The data is split into training and testing sets. Numerical features are standardized using the training-set mean and standard deviation. A neural network with four input neurons, one hidden layer containing eight neurons, and one output neuron is trained using backpropagation.

The dataset is generated for demonstration because the actual Telco Customer Churn dataset is not included with the supplied PDFs. The generated labels follow a simple rule and are not real customer records.

## Note About the Supplied Problem Statement
The PDF first mentions a credit card transactions dataset, including transaction amount normalization and class-imbalance handling. It later describes the Telco Customer Churn dataset and its churn-prediction objective. These are different datasets and tasks. The sample program demonstrates the Telco churn task with generated data; it does not implement credit-card fraud detection, SMOTE, or ROC-AUC.

## Result
A supervised neural network is trained using backpropagation and binary sigmoid activation. The program tests the model on held-out data and displays predictions, accuracy, precision, recall and F1-score.
