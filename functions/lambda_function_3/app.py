def status(code, message):
    return {
        "code: ": code,
        "message": message
    }


def lambda_handler(event, context):
    return status(500, "Internal Error")
