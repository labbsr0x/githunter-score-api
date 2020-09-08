import json

from flask import Response


def get_message(code: str):
    messages = {
        "GENERIC_ERROR": "There was a processing error",
        "OK": "OK",
        "SCHEDULE_ALREADY_EXISTS": "This schedule item already exists.",
        "INTERNAL_ERROR": "There was a processing internal error",
        "SCHEDULE_ITEM_NOT_FOUND": "This schedule item not exist."
    }

    if code in messages:
        return code, messages[code]
    else:
        return "GENERIC_ERROR", messages["GENERIC_ERROR"]


def get_response(status: int, code: str, data=None, error=None):
    message = get_message(code)
    body = {
        "code": code,
        "message": message[1],
        "data": json.loads(data) if data is not None else {},
        "error": str(error) if error is not None else "",
    }
    return Response(json.dumps(body), status=status, mimetype='application/json')


def get_success(data=None):
    return get_response(200, "OK", data)
