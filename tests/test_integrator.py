import json
from api.routes import handle_request
import math

def test_integrate_sin():
    payload = {
        "action": "integrate",
        "samples": 20000,
        "a": 0,
        "b": math.pi,
        "func": "sin"
    }
    resp = json.loads(handle_request(payload))
    # Integral of sin from 0 to pi is 2
    assert abs(resp["integral"] - 2.0) < 0.1

def test_integrate_invalid_func():
    payload = {
        "action": "integrate",
        "samples": 1000,
        "a": 0,
        "b": 1,
        "func": "nonexistent"
    }
    resp = json.loads(handle_request(payload))
    assert "error" in resp
