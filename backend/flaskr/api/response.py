from flask import jsonify, make_response

class CustomResponse:
    def __init__(self):
        self.status: int = 200
        self.message: str = ""
        self.data: dict = {}

    def __repr__(self):
        return f"<Response {self.status}: {self.message}>"

    def __str__(self):
        return f"<Response {self.status}: {self.message}>"

    def __dict__(self):
        self.to_dict()

    def to_dict(self):
        return {"status": self.status, "message": self.message, "data": self.data}


class Response200(CustomResponse):
    def __init__(self, message: str = "Success", data: dict = {}):
        super().__init__()
        self.status = 200
        self.message = message
        self.data = data


class Response201(CustomResponse):
    def __init__(self, message: str = "Created", data: dict = {}):
        super().__init__()
        self.status = 201
        self.message = message
        self.data = data


class Response400(CustomResponse):
    def __init__(self, message: str = "Bad Request"):
        super().__init__()
        self.status = 400
        self.message = message


class Response401(CustomResponse):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__()
        self.status = 401
        self.message = message


class Response404(CustomResponse):
    def __init__(self, message: str = "Not Found"):
        super().__init__()
        self.status = 404
        self.message = message


class Response500(CustomResponse):
    def __init__(self, message: str = "Internal Server Error"):
        super().__init__()
        self.status = 500
        self.message = message


def send_json_response(data: CustomResponse, headers=None):
    """
    Sends a JSON response with the given data and headers.

    Args:
        data (CustomResponse): The data to be converted to JSON and sent as the response body.
        headers (dict, optional): Additional headers to be included in the response. Defaults to None.

    Returns:
        Response: The Flask response object containing the JSON data and headers.
    """
    resp = make_response(jsonify(data.to_dict()), data.status)
    resp.headers.extend(headers or {})
    return resp
