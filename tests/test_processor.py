import json
from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request as WerkzeugRequest

import processor


def run_request(json_body):
    builder = EnvironBuilder(
        method="POST", data=json.dumps(json_body), content_type="application/json"
    )
    env = builder.get_environ()
    req = WerkzeugRequest(env)

    processor.request = req

    response_body, status = processor.main()
    return json.loads(response_body), status


def test_valid_numbers():
    body = {"numbers": [1, 2, 3, 4]}
    result, status = run_request(body)

    assert status == 200
    assert result["count"] == 4
    assert result["sum"] == 10
    assert result["average"] == 2.5


def test_invalid_type():
    body = {"numbers": "oops"}
    result, status = run_request(body)

    assert status == 400
    assert "error" in result


def test_empty_list():
    body = {"numbers": []}
    result, status = run_request(body)

    assert status == 400
    assert "error" in result
