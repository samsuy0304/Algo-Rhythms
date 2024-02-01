# Monte Carlo Integration

Monte Carlo integration is a numerical technique for estimating definite integrals using random sampling. This method is particularly useful when dealing with high-dimensional integrals or integrals that do not have closed-form solutions.

## How Monte Carlo Integration Works

The basic idea behind Monte Carlo integration is to approximate an integral by generating random samples from the domain of integration and using the average function value to estimate the integral. The method is based on the Law of Large Numbers, which states that as the number of random samples increases, the sample average converges to the expected value.

### Formula

The Monte Carlo integration formula for a one-dimensional integral is given by:

$ \[ \int_{a}^{b} f(x) \,dx \approx \frac{1}{N} \sum_{i=1}^{N} f(x_i) \] $

where:
- $N$ is the number of random samples,
- $x_i$ are random samples uniformly distributed in the interval $[a, b]$.

For multidimensional integrals, the formula is extended accordingly:

$ \int_{D} f(\mathbf{x}) \,d\mathbf{x} \approx \frac{1}{N} \sum_{i=1}^{N} f(\mathbf{x}_i) $

where:
- $D$ is the domain of integration,
- $\mathbf{x}_i$ are random samples uniformly distributed in \(D\).

## Importance Sampling

In certain cases, using importance sampling can enhance the efficiency of Monte Carlo integration. Importance sampling involves choosing a probability distribution that is different from the uniform distribution to sample from. The formula is adjusted to account for the sampling distribution:

$ \int_{D} f(\mathbf{x}) \,d\mathbf{x} \approx \frac{1}{N} \sum_{i=1}^{N} \frac{f(\mathbf{x}_i)}{p(\mathbf{x}_i)} $

where:
- $p(\mathbf{x}_i)$ is the probability density function of the chosen distribution.

## Example

Consider the following Python code using NumPy and SciPy for a simple Monte Carlo integration:

```python
import numpy as np
from scipy.stats import multivariate_normal

def monte_carlo_integration(func, num_points, dim, distribution=None):
    points = np.random.rand(num_points, dim) if distribution is None else distribution.rvs(num_points)
    weights = func(points) / (distribution.pdf(points) if distribution is not None else 1.0)
    integral = np.mean(weights)
    return integral
