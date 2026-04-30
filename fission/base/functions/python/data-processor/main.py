# A python function that processes a list of numbers and returns statistics about them.
import json
from flask import request


def process_numbers(numbers):

    if not isinstance(numbers, list):
        raise ValueError("numbers must be a list")

    if not numbers:
        raise ValueError("numbers list is empty")

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers),
    }


def main():
    try:
        payload = request.get_json(force=True)
        result = process_numbers(payload.get("numbers"))
        return json.dumps(result), 200

    except ValueError as e:
        return json.dumps({"error": str(e)}), 400

    except Exception as e:
        return json.dumps({"error": str(e)}), 500
