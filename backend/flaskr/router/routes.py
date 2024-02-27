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
