import math
import numpy as np
from typing import Callable, Tuple

class MonteCarloPi:
    """Estimate π using Monte Carlo sampling.

    Parameters
    ----------
    samples: int
        Number of random points to generate.
    """
    def __init__(self, samples: int):
        self.samples = max(1, samples)

    def run(self) -> Tuple[float, float]:
        """Return (pi_estimate, standard_error)."""
        x = np.random.random(self.samples)
        y = np.random.random(self.samples)
        inside = (x * x + y * y) <= 1.0
        proportion = np.mean(inside)
        pi_est = 4 * proportion
        # Standard error of proportion * 4
        std_err = 4 * math.sqrt(proportion * (1 - proportion) / self.samples)
        return pi_est, std_err

class MonteCarloIntegrator:
    """Estimate a definite integral using Monte Carlo.

    Parameters
    ----------
    samples: int
        Number of random samples.
    a, b: float
        Integration limits (a < b).
    func_name: str
        Name of a NumPy math function, e.g. "sin", "exp".
    """
    def __init__(self, samples: int, a: float, b: float, func_name: str):
        if a >= b:
            raise ValueError("Lower limit a must be less than upper limit b")
        self.samples = max(1, samples)
        self.a = a
        self.b = b
        self.func = self._resolve_func(func_name)

    def _resolve_func(self, name: str) -> Callable[[np.ndarray], np.ndarray]:
        if not hasattr(np, name):
            raise ValueError(f"Function '{name}' not found in numpy")
        return getattr(np, name)

    def run(self) -> Tuple[float, float]:
        """Return (integral_estimate, standard_error)."""
        xs = np.random.uniform(self.a, self.b, self.samples)
        fx = self.func(xs)
        mean_fx = np.mean(fx)
        integral = (self.b - self.a) * mean_fx
        # Standard error of the mean times interval length
        std_err = (self.b - self.a) * np.std(fx, ddof=1) / math.sqrt(self.samples)
        return float(integral), float(std_err)
