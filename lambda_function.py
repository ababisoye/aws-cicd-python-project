import json

from app import calculate_rental_cost


def lambda_handler(event, context):
    hours = event["hours"]
    hourly_rate = event["hourly_rate"]

    total = calculate_rental_cost(hours, hourly_rate)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Rental cost calculated successfully",
            "total":total
        })
    }
