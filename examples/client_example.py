import json
from pathlib import Path
from api.routes import handle_request

def main():
    # Estimate pi with 50000 samples
    pi_payload = {"action": "estimate_pi", "samples": 50000}
    pi_result = json.loads(handle_request(pi_payload))
    # Integrate exp from 0 to 1
    integ_payload = {
        "action": "integrate",
        "samples": 50000,
        "a": 0,
        "b": 1,
        "func": "exp"
    }
    integ_result = json.loads(handle_request(integ_payload))
    output = {
        "pi": pi_result,
        "exp_integral": integ_result
    }
    out_path = Path(__file__).parent.parent / "results" / "output.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2))
    print(f"Results written to {out_path}")

if __name__ == "__main__":
    main()
