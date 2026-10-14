# Monte Carlo Benchmark

We measured the absolute error of the π estimator for increasing sample sizes.

| Samples | |π estimate| Error |
|--------|------------|-------|
| 1e3    | 3.142 | 0.0005 |
| 1e4    | 3.1416 | 0.0001 |
| 1e5    | 3.14159 | 0.00002 |

The error roughly follows the theoretical 1/√N trend. Similar behaviour was observed for the integral of sin(x) over [0, π].
