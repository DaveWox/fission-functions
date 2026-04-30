# A python function that processes a list of numbers and returns statistics about them.
import json
import os
from flask import request
from prometheus_client import Counter

# Set up Prometheus metrics exporter
FUNCTION_NAME = os.getenv("FUNCTION_NAME", "data_processor")
PROCESS_COUNT = Counter("fission_function_process_count", "Total number of requests processed", ["function"])
PROCESS_TIME = Counter("fission_function_process_time", "Total time spent processing requests", ["function"])

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
        # Increment the process count and time metrics
        PROCESS_COUNT.labels(function=FUNCTION_NAME).inc()
        PROCESS_TIME.labels(function=FUNCTION_NAME).inc()

        payload = request.get_json(force=True)
        result = process_numbers(payload.get("numbers"))
        return json.dumps(result), 200

    except ValueError as e:
        return json.dumps({"error": str(e)}), 400

    except Exception as e:
        return json.dumps({"error": str(e)}), 500
