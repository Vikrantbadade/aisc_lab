# ANFIS for Household Energy Consumption Prediction

## Aim
To design and implement an Adaptive Neuro-Fuzzy Inference System (ANFIS) to predict daily household energy consumption based on temperature, humidity, appliance usage and occupancy.

## Theory
The Adaptive Neuro-Fuzzy Inference System (ANFIS) integrates fuzzy logic and artificial neural networks into a hybrid model.

- The fuzzy inference system provides reasoning under uncertainty using linguistic rules.
- The neural network component tunes fuzzy membership functions and rule parameters through learning.

ANFIS is useful for modeling nonlinear relationships where explicit mathematical models are difficult to derive.

## Key Features
### Sugeno-Type Fuzzy Inference System
ANFIS uses a Sugeno-type fuzzy inference system. Its rule outputs are numerical equations, which are suitable for optimization and learning.

Example rule:

`IF Temperature is High AND Humidity is Low THEN EnergyConsumption = 0.5 × Temperature + 0.3 × Humidity`

### Hybrid Learning
ANFIS adjusts two types of parameters:

- Premise parameters define the shape and position of membership functions.
- Consequent parameters define the linear equation coefficients in each fuzzy rule.

The hybrid learning method combines:

- Least Squares Estimation (LSE): adjusts consequent parameters.
- Gradient Descent: updates premise parameters.

## Problem Statement
Predict household energy consumption using the following inputs:

| Input | Description |
|---|---|
| Temperature | Temperature in °C |
| Humidity | Humidity in % |
| Occupancy | 0/1 or number of persons |
| Appliances | Total appliance power or appliance count |
| HourOfDay | Hour from 0 to 23 (optional) |

Output: `EnergyConsumption`, measured in kWh per time step. This is a regression problem.

## ANFIS Architecture
1. Layer 1 – Fuzzification: compute membership values for each input membership function.
2. Layer 2 – Rule layer: calculate rule firing strengths using the product or minimum of input membership values.
3. Layer 3 – Normalization: normalize the firing strengths.
4. Layer 4 – Consequent / defuzzification: calculate rule outputs using linear consequent functions.
5. Layer 5 – Output: aggregate rule outputs to produce the final numerical prediction.

## Procedure
1. Define the input and output variables.
2. Use training-set minimum and maximum values to define input ranges.
3. Select membership functions and initialize their centers and widths.
4. Generate fuzzy rules.
5. Implement the five-layer ANFIS architecture.
6. Train using least squares and gradient descent.
7. Evaluate on test data using RMSE, MAE and R².
8. Plot predicted versus actual energy consumption.
9. Analyze learned rules and adapted membership functions.

## Implementation Note
The PDF does not provide a household energy dataset or numerical membership-function parameters. The accompanying Python program therefore generates a reproducible synthetic dataset for demonstration. It uses two Gaussian membership functions per input, giving 32 rules for five inputs. It demonstrates a compact Sugeno-style neuro-fuzzy regression model and hybrid parameter adjustment; it is not trained on measured household energy records.

## Result
The program trains a Sugeno-style ANFIS demonstration model and reports RMSE, MAE and R² on held-out synthetic data. It also plots predicted versus actual energy consumption and the input membership functions.

## Requirements
Install the required libraries using:

`pip install numpy matplotlib`
