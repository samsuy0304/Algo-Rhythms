# Random Number Generator

This project implements a random number generator class in Python. The `Random` class generates random numbers, floating-point numbers, and follows various probability distributions such as Bernoulli, Exponential, Binomial, and Categorical.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Example](#example)

## Introduction

The `Random` class provides a versatile random number generator with support for various distributions commonly used in statistical simulations and modeling.

## Features

- Generation of random 64-bit integers.
- Random floating-point numbers between (0, 1) (uniform distribution).
- Random integers (0 or 1) according to a Bernoulli distribution.
- Random doubles according to an exponential distribution.
- Random numbers of success after `n` trials according to a binomial distribution.
- Random integers that index categories provided in a probability list (Categorical distribution).
- Generation of random numbers within a specified range.

## Usage

1. Import the `Random` class into your Python script:

    ```python
    from random_generator import Random
    ```

2. Create an instance of the `Random` class:

    ```python
    random_gen = Random(seed=5555)
    ```

3. Use the various methods of the `Random` class to generate random numbers and distributions.

## Example

```python
# Import the Random class
from random_generator import Random

# Create an instance of the Random class
random_gen = Random(seed=5555)

# Generate a random 64-bit integer
random_int = random_gen.int64()

# Generate a random floating-point number between (0, 1)
random_float = random_gen.rand()

# Generate a random integer (0 or 1) according to a Bernoulli distribution
random_bernoulli = random_gen.Bernoulli(p=0.5)

# Generate a random double according to an exponential distribution
random_exponential = random_gen.Exponential(beta=1.0)

# Generate a random number of success after 10 trials according to a binomial distribution
random_binomial = random_gen.Binomial(n=10, p=0.5)

# Generate a random integer that indexes categories provided in a probability list
random_categorical = random_gen.Categorical(p=[0.5, 0.5])

# Generate a list of random numbers within a specified range
random_range = random_gen.Random_Range(a=0, b=1, N=10)

print(random_int, random_float, random_bernoulli, random_exponential, random_binomial, random_categorical, random_range)
