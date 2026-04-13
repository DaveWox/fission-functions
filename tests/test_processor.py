import json
import types
from processor import main
from flask import Request
from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request as WerkzeugRequest

def run_request(json_body):
    builder = EnvironBuilder(
        method="POST",
        data=json.dumps(json_body),
        content_type="application/json"
    )
    env = builder.get_environ()
    req = WerkzeugRequest(env)

    # Monkey‑patch Flask's global request object
    import processor
    processor.request = req

    result, status = main()
    return json.loads(result), status


def test_valid_numbers():
    body = {"numbers": [1, 2, 3, 4]}
    json_out, status = run_request(body)
    assert status == 200
    assert json_out["sum"] == 10
    assert json_out["average"] == 2.5


def test_invalid_type():
    body = {"numbers": "oops"}
    json_out, status = run_request(body)
    assert status == 400


def test_empty_list():
    body = {"numbers": []}
    json_out, status = run_request(body)
    assert status == 400
