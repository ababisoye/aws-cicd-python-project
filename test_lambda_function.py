import json

from lambda_function import lambda_handler


def test_lambda_handler():
    event = {
        "hours": 6,
        "hourly_rate": 5000
    }

    response = lambda_handler(event, None)

    assert response["statusCode"] == 200
    assert json.loads(response["body"]) == {
        "message": "Rental cost calculated successfully",
        "total": 30000
    }
