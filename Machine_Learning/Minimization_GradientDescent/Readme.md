# Minimization Methods

Minimization methods are numerical techniques for finding the minimum of a function. These methods are essential in optimization problems where the goal is to locate the minimum of a cost or objective function.

## Types of Minimization Methods

### 1. **Gradient Descent**

Gradient descent is an iterative optimization algorithm that uses the gradient (derivative) of the function to find the minimum. It updates the parameters in the opposite direction of the gradient until convergence.

#### Formula

For a parameter vector $\mathbf{x}$ and a scalar-valued function $f(\mathbf{x})$, the update rule for gradient descent is given by:

$ \mathbf{x}_{\text{new}} = \mathbf{x}_{\text{old}} - \alpha \nabla f(\mathbf{x}_{\text{old}}) $

where:
- $\alpha$ is the learning rate,
- $\nabla f(\mathbf{x})$ is the gradient of $f$ with respect to $\mathbf{x}$.

### 2. **Newton's Method**

Newton's method is an iterative optimization algorithm that uses both the first and second derivatives of the function. It provides faster convergence but may not always converge to the global minimum.

#### Formula

The update rule for Newton's method is given by:

$ \mathbf{x}_{\text{new}} = \mathbf{x}_{\text{old}} - H^{-1} \nabla f(\mathbf{x}_{\text{old}}) $

where:
- $H$ is the Hessian matrix (second derivative) of $f$.

## Example Python Code

```python
import numpy as np
from scipy.optimize import minimize

# Define the function to be minimized
def quadratic_function(x):
    return x**2 + 3*x + 5

# Perform minimization using scipy.optimize.minimize
result = minimize(quadratic_function, x0=0)

# Display the result
print(f"Minimum found at x = {result.x}")
print(f"Minimum function value = {result.fun}")
