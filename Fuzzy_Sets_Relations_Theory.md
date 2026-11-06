# Fuzzy Sets and Fuzzy Relations for AQI and Health Effects

## Aim
To implement fuzzy sets and fuzzy relations and model the relationship between Air Quality Index (AQI) values and their corresponding health effects.

## Theory
In classical set theory, an element either belongs to a set (membership 1) or does not belong (membership 0). A fuzzy set allows partial membership, where each element has a membership value between 0 and 1.

A fuzzy set A in universe X is defined as:

`A = {(x, μA(x)) | x ∈ X}`

The membership function μA(x) assigns a degree of belonging to each element. Fuzzy sets model imprecision and vagueness and provide smooth transitions instead of strict cutoffs.

## Fuzzy Operations
For fuzzy sets A and B, the program implements:

- Algebraic Sum: `μ(A ∪ B) = μA + μB − μA × μB`
- Algebraic Product: `μ(A ∩ B) = μA × μB`
- Bounded Sum: `μ(A ∪ B) = min(μA + μB, 1)`
- Bounded Difference: `μ(A − B) = max(μA − μB, 0)`

## Problem Statement: AQI and Health Effects
The practical models the relationship between AQI values and health effects.

### Fuzzy Sets

- Set A – Air Quality Levels: Good (G), Moderate (M), Poor (P), Severe (S).
- Set B – Health Effects: Healthy (H), Mild Symptoms (MS), Serious Symptoms (SS).
- Set C – Desired Health Condition: Healthy (H), Mild Symptoms (MS), Serious Symptoms (SS).

The program defines membership functions for the four AQI categories and the three health-effect categories. It then computes a fuzzy relation using the Cartesian-product principle and performs Max-Min and Max-Product composition.

### Examples from the Practical
- AQI = 40: strong membership in Good Air Quality, mostly Healthy.
- AQI = 120: membership in Moderate and Poor, may cause Mild Symptoms.
- AQI = 250: high membership in Severe, likely Serious Symptoms.

## Procedure
1. Define fuzzy sets for AQI categories.
2. Define fuzzy sets for health effects.
3. Define the desired health condition.
4. Perform union, intersection, bounded sum and bounded difference.
5. Compute the Cartesian product between AQI levels and health effects.
6. Perform Max-Min composition.
7. Perform Max-Product composition.
8. Plot and analyze the membership functions and results.

## Implementation Note
The PDF specifies the fuzzy categories and operations but does not provide numerical membership-function parameters or a fixed AQI universe. The Python program therefore uses illustrative AQI sample values and explicitly defined membership functions. The resulting relation and compositions depend on these chosen values; they are a demonstration of the specified method, not official medical or AQI thresholds.

## Result
Fuzzy sets and fuzzy operations are implemented. The program calculates the AQI-health fuzzy relation, Max-Min composition and Max-Product composition, and plots the membership functions.
