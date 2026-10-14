import json
from api.routes import handle_request

def test_pi_estimate_basic():
    payload = {"action": "estimate_pi", "samples": 10000}
    response = json.loads(handle_request(payload))
    assert "pi_estimate" in response
    assert abs(response["pi_estimate"] - 3.1415) < 0.1

def test_pi_estimate_edge_zero_samples():
    payload = {"action": "estimate_pi", "samples": 0}
    response = json.loads(handle_request(payload))
    # With zero samples we default to 1 sample, error should be maximal
    assert response["error"] >= 4.0
