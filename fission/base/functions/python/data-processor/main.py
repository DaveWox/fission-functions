# A python function that processes a list of numbers and returns statistics about them.
import json
from flask import request

def main():
    """
    Fission Python functions receive HTTP requests through Flask's request object.
    """
    try:
        payload = request.get_json(force=True)
        numbers = payload.get("numbers", [])

        if not isinstance(numbers, list):
            return json.dumps({"error": "numbers must be a list"}), 400

        if not numbers:
            return json.dumps({"error": "numbers list is empty"}), 400

        result = {
            "count": len(numbers),
            "sum": sum(numbers),
            "min": min(numbers),
            "max": max(numbers),
            "average": sum(numbers) / len(numbers),
        }

        return json.dumps(result), 200

    except Exception as e:
        return json.dumps({"error": str(e)}), 500
