# Fuzzy Logic Controller for Traffic Light Duration

## Aim
To design and implement a Fuzzy Logic Controller (FLC) that dynamically adjusts the green light duration at an intersection based on traffic density and waiting time, ensuring smoother traffic flow and reduced congestion.

## Theory
A Fuzzy Logic Controller is a control system based on fuzzy set theory. It models human reasoning and decision-making using linguistic rules rather than precise mathematical equations.

The controller accepts crisp input values, converts them into fuzzy membership values, applies IF–THEN rules, combines the rule outputs and converts the result into a crisp output.

## 1. Identification of Variables

### Input Variables

| Variable | Range | Fuzzy sets |
|---|---:|---|
| Traffic density | 0–50 vehicles/min | Low, Medium, High |
| Waiting time | 0–120 seconds | Short, Moderate, Long |

### Output Variable

| Variable | Range | Fuzzy sets |
|---|---:|---|
| Green light duration | 10–90 seconds | Short, Medium, Long |

## 2. Fuzzy Subset Configuration and Membership Functions

The program uses trapezoidal and triangular membership functions.

### Traffic Density
- Low: trapezoidal membership function over 0–15 vehicles/min.
- Medium: triangular membership function over 10–30 vehicles/min.
- High: trapezoidal membership function over 25–50 vehicles/min.

### Waiting Time
- Short: trapezoidal membership function over 0–30 seconds.
- Moderate: triangular membership function over 20–80 seconds.
- Long: trapezoidal membership function over 70–120 seconds.

### Green Light Duration
- Short: 10–30 seconds.
- Medium: 30–60 seconds.
- Long: 60–90 seconds.

The code selects explicit membership-function parameters within these ranges to provide overlapping fuzzy sets.

## 3. Fuzzy Rule Base

The controller uses the following nine rules:

| Rule | Traffic density | Waiting time | Green duration |
|---:|---|---|---|
| 1 | Low | Short | Short |
| 2 | Low | Moderate | Short |
| 3 | Low | Long | Medium |
| 4 | Medium | Short | Medium |
| 5 | Medium | Moderate | Medium |
| 6 | Medium | Long | Long |
| 7 | High | Short | Medium |
| 8 | High | Moderate | Long |
| 9 | High | Long | Long |

These rules increase green time when traffic density or waiting time is high.

## 4. Fuzzification
Fuzzification converts crisp sensor readings into membership degrees between 0 and 1.

For example, the practical PDF gives an example with 35 vehicles and 100 seconds waiting time:
- Medium density membership = 0.6
- High density membership = 0.4
- Moderate waiting membership = 0.2
- Long waiting membership = 0.8

## 5. Inference Mechanism
The program uses Mamdani inference. The AND operator is implemented using the minimum of the input membership degrees.

For example:

`IF Density is High AND Waiting is Long THEN Green Duration is Long`

`μ(Long) = min(0.4, 0.8) = 0.4`

## 6. Aggregation
The output fuzzy sets from all activated rules are combined using the maximum operator to form one aggregated fuzzy output.

## 7. Defuzzification
The centroid of gravity method converts the aggregated fuzzy output into a crisp green-light duration.

`Green Duration = Σ(x × μ(x)) / Σμ(x)`

The result is expressed in seconds.

## 8. Implementation and Testing
The Python program:
1. Defines input and output universes.
2. Creates triangular and trapezoidal membership functions.
3. Defines the nine fuzzy rules.
4. Fuzzifies traffic density and waiting time.
5. Applies Mamdani inference and aggregates the rule outputs.
6. Uses centroid defuzzification to calculate green-light duration.
7. Tests low, medium and high traffic conditions.
8. Plots membership functions and the control surface.

## Result
The Fuzzy Logic Controller calculates a green-light duration based on traffic density and waiting time. Low traffic with a short wait receives a shorter green duration, while high traffic and long waiting time receive a longer duration.

## Implementation Note
The PDF specifies the fuzzy-set ranges and gives two example rules, but it does not provide exact membership-function coordinates for every set or a complete rule table. The program uses explicit overlapping membership-function parameters and a nine-rule base as a practical implementation choice. These design choices can be adjusted for a real intersection after traffic measurements and safety constraints are established.

The program is a simulation. It does not connect to physical traffic lights or replace traffic-signal safety controls.

## Requirements
Install the required libraries using:

`pip install numpy matplotlib`

## Sample Inputs
- Low traffic: 5 vehicles/min, 10 seconds waiting.
- Medium traffic: 20 vehicles/min, 50 seconds waiting.
- High traffic: 40 vehicles/min, 100 seconds waiting.
