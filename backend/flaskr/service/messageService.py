from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance
from twilio.base.exceptions import TwilioRestException
import os
from flaskr.models.models import User


class MessageService:
    def __init__(self):
        self.TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
        self.TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
        self.TWILIO_MESSAGE_SERVICE_SID = os.environ.get("TWILIO_MESSAGE_SERVICE_SID")
        self.EMAIL_API_KEY = os.environ.get("EMAIL_API_KEY")
        self.EMAIL_API_SECRET = os.environ.get("EMAIL_API_SECRET")
        self.EMAIL_API_URL = os.environ.get("EMAIL_API_URL")
        self.EMAIL_API_FROM = os.environ.get("EMAIL_API_FROM")

    def send_alert(self, method: str, userList: list[User], message: str) -> bool:
        """Sends alert to users based on the method provided

        Keyword arguments:
        method -- this can be "SMS" or "EMAIL"
        Return: True if successful, False if not
        """

        if method == "SMS":
            for user in userList:
                self.send_sms(message=message, to=user.phone_number)
        elif method == "EMAIL":
            for user in userList:
                self.send_email(message=message, to=user.email)
        else:
            raise ValueError(
                f"Invalid method: {method}. Allowed methods are: SMS, EMAIL"
            )

    # --------------------------------------------------------------------------
    # Private Methods

    def send_sms(self, message: str, to: str = "") -> str:
        try:
            client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)
            message: MessageInstance = client.messages.create(
                body=message,
                messaging_service_sid=self.TWILIO_MESSAGE_SERVICE_SID,
                to=to,
            )
            return message.sid
        except TwilioRestException as e:
            raise e
        except Exception as e:
            raise e

    def send_email(self, message: str, to: str) -> str:
        # Send email logic here
        print("Sending Email")
