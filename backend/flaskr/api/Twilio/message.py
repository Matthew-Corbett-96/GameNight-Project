# from flask import Response, request
# from flask_restful import Resource, Api
# from ...models.models import *
# from ..response import Response200, Response404, send_json_response
# from twilio.rest import Client
# from twilio.twiml.messaging_response import MessagingResponse
# import os

# class TwilioClass(Resource):
#    def post(self) -> Response:
#       data = request.json
#       print(data)
#       client = Client(data["account_sid"], data["auth_token"])
#       message = client.messages.create(
#             body=data["message"],
#             messaging_service_sid= os.environ.get("TWILIO_MESSAGING_SERVICE_SID"),
#             to=data["to"]
#       )
#       return send_json_response(Response200(data={"message": message.to_dict()}))