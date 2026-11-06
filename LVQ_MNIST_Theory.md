# Learning Vector Quantization (LVQ) on MNIST Digits

## Aim
To implement Learning Vector Quantization (LVQ) for digit classification.

## Theory
Learning Vector Quantization (LVQ) is a prototype-based classification algorithm. Each class is represented by one or more prototype vectors. During training, the algorithm finds the prototype closest to the input vector.

- If the winning prototype belongs to the correct class, it is moved closer to the input.
- If the winning prototype belongs to a different class, it is moved away from the input.

Over time, the prototypes become representatives of their classes and form decision boundaries. LVQ is useful for multiclass classification when labelled data is available.

## Dataset and Procedure
The practical uses the handwritten digit dataset available through `sklearn.datasets.load_digits`.

1. Load the digit data and labels.
2. Standardize the input features.
3. Split the data into training and testing sets.
4. Initialize three prototypes for each digit class using the class mean with small random noise.
5. Train the prototypes using the LVQ update rule for 50 epochs.
6. For each test sample, select the nearest prototype and use its class as the prediction.
7. Calculate test accuracy.

## Result
The LVQ algorithm classifies handwritten digits and displays the test accuracy.

## Requirements
Install the required libraries using:

`pip install numpy scikit-learn`
