from logging import getLogger
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

    def sendGameDayAlert(self, userList: list[User]) -> None:
        """Sends alert to users on game day

        Keyword arguments:
        userList -- list of users to send the alert to
        Return: None
        """
    
        message = "Hello, it's game day! Don't forget to join the games at 730pm."
        self.send_alert("SMS", userList, message)

    def sendDayBeforeAlert(self, userList: list[User]) -> None:
        """Sends alert to users the day before the game

        Keyword arguments:
        userList -- list of users to send the alert to
        Return: None
        """
        message = "Hello, don't forget to join the game tomorrow at 730pm. While you cannot RSVP here (yet) please let the host know if you plan to attend. Thanks!"
        self.send_alert("SMS", userList, message)

    def sendHourOnHourMessage(self, userList: list[User]) -> None:
        """Sends alert to users every hour on the hour

        Keyword arguments:
        userList -- list of users to send the alert to
        Return: None
        """
        message = "Every hour on the hour, you know what to do!"
        self.send_alert("SMS", userList, message)

   # --------------------------------------------------------------------------
   # Private Methods
    def send_alert(self, method: str, userList: list[User], message: str) -> bool:
        """Sends alert to users based on the method provided

        Keyword arguments:
        method -- this can be "SMS" or "EMAIL"
        Return: True if successful, False if not
        """

        logger = getLogger(__name__)
        if method == "SMS":
            logger.info("Sending SMS...")
            logger.info(f'Env Var: {self.TWILIO_ACCOUNT_SID}  ///  {self.TWILIO_AUTH_TOKEN}  ///  {self.TWILIO_MESSAGE_SERVICE_SID}')
            for user in userList:
                self.send_sms(message=message, to=user.phone_number)
        elif method == "EMAIL":
            for user in userList:
                self.send_email(message=message, to=user.email)
        else:
            raise ValueError(
                f"Invalid method: {method}. Allowed methods are: SMS, EMAIL"
            )

    def send_sms(self, message: str, to: str = "") -> str:
        try:
            print(f"Sending Game Day Alert: {to}")
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
