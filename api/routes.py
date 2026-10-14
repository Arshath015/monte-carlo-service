import json
from typing import Any, Dict
from core.monte_carlo import MonteCarloPi, MonteCarloIntegrator

def handle_request(payload: Dict[str, Any]) -> str:
    """Process a simulated request payload.

    The payload must contain an ``action`` key. Supported actions:
    * ``estimate_pi`` – requires ``samples`` (int).
    * ``integrate`` – requires ``samples`` (int), ``a`` (float), ``b`` (float), ``func`` (str).
    Returns a JSON string with the result.
    """
    action = payload.get("action")
    if action == "estimate_pi":
        samples = int(payload.get("samples", 1000))
        estimator = MonteCarloPi(samples)
        pi_est, err = estimator.run()
        result = {"pi_estimate": pi_est, "error": err}
    elif action == "integrate":
        samples = int(payload.get("samples", 1000))
        a = float(payload["a"])
        b = float(payload["b"])
        func_name = payload["func"]
        integrator = MonteCarloIntegrator(samples, a, b, func_name)
        integral, err = integrator.run()
        result = {"integral": integral, "error": err}
    else:
        result = {"error": "Unsupported action"}
    return json.dumps(result)
