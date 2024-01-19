from flask import request
from flask_restful import Resource, Api
from flaskr.models.models import Game, db
from .response import Response200, Response404, Response401, send_json_response

from flask_sqlalchemy import SQLAlchemy


class GameRestClass(Resource):
    def get(self, game_id=None):
        if game_id is None:
            games_dict = [game.to_dict() for game in Game.query.all()]
            return send_json_response(Response200(data={"games": games_dict}))

        game = Game.query.filter_by(id=game_id).first()
        if game is None:
            return send_json_response(Response404("Game Not Found"))

        return send_json_response(Response200(data={"game": game.to_dict()}))

    def post(self):
        data = request.json

        # Check if game name is already taken
        if Game.query.filter_by(name=data["name"]).first() is not None:
            return send_json_response(
                Response401(message=f"Game Name '{data.get('name')}' Already Exists")
            )

        game = Game(
            name=data.get("name"),
            description=data.get("description"),
            min_players=data.get("min_players"),
            max_players=data.get("max_players"),
        )
        db.session.add(game)
        db.session.commit()
        return send_json_response(Response200(data={"game": game.to_dict()}))

    def put(self, game_id):
        data = request.json
        # Check if game exists
        game = Game.query.filter_by(id=game_id).first()
        if game is None:
            return send_json_response(Response404("Game Not Found"))

        # Check if game name is already taken
        if data.get("name", None) is not None:
            if data["name"] != game.name:
                if Game.query.filter_by(name=data["name"]).first() is not None:
                    return send_json_response(
                        Response401(
                            message=f"Game Name '{data.get('name')}' Already Exists"
                        )
                    )

        game.name = data.get("name", game.name)
        game.description = data.get("description", game.description)
        game.min_players = data.get("min_players", game.min_players)
        game.max_players = data.get("max_players", game.max_players)
        db.session.commit()

        return send_json_response(Response200(data={"game": game.to_dict()}))

    def delete(self, game_id):
        game = Game.query.filter_by(id=game_id).first()
        if game is None:
            return send_json_response(Response404("Game Not Found"))

        db.session.delete(game)
        db.session.commit()
        return send_json_response(Response200(f"{game_id} Deleted"))


def setup_routes_for_game(api: Api) -> None:
    api.add_resource(GameRestClass, "/games/", "/games/<uuid:game_id>")
