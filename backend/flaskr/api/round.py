from flask import Response, request
from flask_restful import Resource, Api
from ..models.models import db, Game, GameNight, Round
from .response import Response200, Response404, send_json_response

# Round model
class RoundRestClass(Resource):
    def get(self, round_id=None) -> Response:
        if round_id is None:
            results_dict = [round.to_dict() for round in Round.query.all()]
            return send_json_response(Response200(data={"rounds": results_dict}))

        round: Round = Round.query.filter_by(id=round_id).first()
        if round is None:
            return send_json_response(Response404("Round Not Found"))

        return send_json_response(Response200(data={"round": round.to_dict()}))

    def post(self) -> Response:
        data = request.json

        game_night = GameNight.query.filter_by(id=data["game_night_id"]).first()
        if game_night is None:
            return send_json_response(Response404("Game Night Not Found"))

        game = Game.query.filter_by(name=data["game"]).first()
        if game is None:
            return send_json_response(Response404("Game Not Found"))

        round: Round = Round(
            game_night_id=game_night.id, 
            game_id=game.id,
            notes=data.get("notes", None)
        )
        db.session.add(round)
        db.session.commit()
        return send_json_response(Response200(data={"round": round.to_dict()}))

    def put(self, round_id) -> Response:
        data = request.json

        round: Round = Round.query.filter_by(id=round_id).first()
        if round is None:
            return send_json_response(Response404("Round Not Found"))

        round.game_night_id = data.get("game_night_id", round.game_night_id)
        round.game_id = data.get("game_id", round.game_id)
        db.session.commit()
        return send_json_response(Response200(data={"round": round.to_dict()}))

    def delete(self, round_id) -> Response:
        round: Round = Round.query.filter_by(id=round_id).first()
        if round is None:
            return send_json_response(Response404("Round Not Found"))

        db.session.delete(round)
        db.session.commit()
        return send_json_response(Response200(f"{round_id} Deleted"))

def setup_routes_for_round(api: Api) -> None:
      api.add_resource(RoundRestClass, "/rounds/", "/rounds/<uuid:round_id>")