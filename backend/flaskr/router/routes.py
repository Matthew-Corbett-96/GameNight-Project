from logging import getLogger
from flask import Flask, Response, Request, request
from flask_restful import Api
from ..api.response import (
    Response200,
    Response400,
    Response404,
    Response500,
    send_json_response,
)
from ..api.user import setup_routes_for_user
from ..api.Auth0.auth import setup_routes_for_auth0
from ..api.game import setup_routes_for_game
from ..api.gamenight import setup_routes_for_game_night
from ..api.round import setup_routes_for_round
from ..api.rsvp import setup_routes_for_rsvp_log
from ..api.role import setup_routes_for_user_role
from ..api.notification import setup_routes_for_notification
from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance
from twilio.base.exceptions import TwilioRestException
import os
from flaskr.tasks import simple_test
from flaskr.models.models import User


def setup_routes(app: Flask, api: Api) -> None:
    # Add resources to api
    setup_routes_for_auth0(api)
    setup_routes_for_user(api)
    setup_routes_for_game(api)
    setup_routes_for_game_night(api)
    setup_routes_for_round(api)
    setup_routes_for_rsvp_log(api)
    setup_routes_for_notification(api)
    setup_routes_for_user_role(api)

    # Healthcheck
    @app.route("/healthcheck", methods=["GET"])
    def heathcheck() -> Response:
        return send_json_response(Response200("Healthy"))

    # 404
    @app.errorhandler(404)
    def not_found(error) -> Response:
        return send_json_response(Response404("Page Not Found"))

    # 500
    @app.errorhandler(500)
    def internal_server_error(error) -> Response:
        return send_json_response(Response500())

    # 400
    @app.errorhandler(400)
    def bad_request(error) -> Response:
        return send_json_response(Response400())

    @app.route("/test", methods=["GET"])
    def test() -> Response:
        try:
            account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
            auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
            messageservicesid = os.environ.get("TWILIO_MESSAGE_SERVICE_SID")
            client = Client(account_sid, auth_token)

            messageId = client.messages.create(
                messaging_service_sid=messageservicesid, body="Test", to="+15082438026"
            )
            return send_json_response(Response200(f"Message sent: {messageId.sid}"))
        except TwilioRestException as e:
            raise e
        except Exception as e:
            raise e

    @app.route("/test2", methods=["GET"])
    def test2() -> Response:
        logger = getLogger(__name__)
        logger.info("Test2")
        simple_test.delay()
        return send_json_response(Response200(message="Task Sent", data=None))
