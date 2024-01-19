from flask import Response, request
from flask_restful import Api, Resource
from ..models.models import db, GameNight
from .response import Response200, Response404, send_json_response


class GameNightRestClass(Resource):
    def get(self, game_night_id=None) -> Response:
        if game_night_id is None:
            game_nights_dict = [
                game_night.to_dict() for game_night in GameNight.query.all()
            ]
            return send_json_response(
                Response200(data={"game_nights": game_nights_dict})
            )

        game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
        if game_night is None:
            return send_json_response(Response404("Game Night Not Found"))

        return send_json_response(
            Response200(data={"game_night": game_night.to_dict()})
        )

    def post(self) -> Response:
        data = request.json
        game_night: GameNight = GameNight(date=data["date"])
        db.session.add(game_night)
        db.session.commit()
        return send_json_response(
            Response200(data={"game_night": game_night.to_dict()})
        )

    def put(self, game_night_id) -> Response:
        data = request.json
        game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
        if game_night is None:
            return send_json_response(Response404("Game Night Not Found"))

        game_night.date = data["date"]
        db.session.commit()
        return send_json_response(
            Response200(data={"game_night": game_night.to_dict()})
        )

    def delete(self, game_night_id) -> Response:
        game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
        if game_night is None:
            return send_json_response(Response404("Game Night Not Found"))

        db.session.delete(game_night)
        db.session.commit()
        return send_json_response(Response200(f"{game_night_id} Deleted"))


def setup_routes_for_game_night(api: Api) -> None:
    api.add_resource(
        GameNightRestClass, "/gamenights/", "/gamenights/<uuid:game_night_id>"
    )
