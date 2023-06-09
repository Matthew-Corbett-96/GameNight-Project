from flask import Flask, Response, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from ..models.models import db, User, Game, GameNight, GameNightGame
from uuid import UUID # used for generating unique ids


def setup_routes(app: Flask, api: Api) -> None:
    class GameRestClass(Resource):
        def get(self, game_id: str = None) -> Response:
            if game_id is None:
                games = Game.query.all()
                games_dict = [
                    game.to_dict() for game in games   # convert each game to a dictionary
                ]
                return make_response(jsonify(games_dict), 200)

            game_id_uuid = UUID(game_id)
            game: Game = Game.query.filter_by(id=game_id_uuid).first()
            if game:
                return make_response(jsonify(game.to_dict()), 200)
            
            return make_response(jsonify({"message": "Game not found."}), 404)

        def post(self):
            data = request.json
            game: Game = Game(
                name=data["name"],
                description=data["description"],
                game_type=data["game_type"],
                min_players=data["min_players"],
                max_players=data["max_players"],
            )
            db.session.add(game)
            db.session.commit()
            return make_response(jsonify(game.to_dict()), 200)

        def put(self, game_id):
            game_id = UUID(game_id)
            data = request.json
            game: Game = Game.query.filter_by(id=game_id).first()
            if game:
                game.name = data["name"]
                game.description = data["description"]
                game.game_type = data["game_type"]
                game.min_players = data["min_players"]
                game.max_players = data["max_players"]
                db.session.commit()
                return make_response(jsonify(game.to_dict()), 200)
            
            return make_response(jsonify({"message": "Game not found."}), 404)

        def delete(self, game_id):
            game_id = UUID(game_id)
            game: Game = Game.query.filter_by(id=game_id).first()
            if game:
               db.session.delete(game)
               db.session.commit()
               return make_response(f"{game} was removed.", 200)
            
            return make_response(jsonify({"message": "Game not found."}), 404)

    api.add_resource(GameRestClass, "/games/", "/games/<string:game_id>")

    # User model
    class UserRestClass(Resource):
        def get(self, user_id=None):
            if user_id is None:
                users = User.query.all()
                users_dict = [user.to_dict() for user in users]
                return make_response(jsonify(users_dict), 200)

            user_id: UUID = UUID(user_id)
            user: User = User.query.filter_by(id=user_id).first()
            if user:
               return make_response(jsonify(user.to_dict()), 200)
            
            return make_response(jsonify({"message": "User not found."}), 404)

    api.add_resource(UserRestClass, "/users/", "/users/<string:user_id>")

    @app.route("/healthcheck", methods=["GET"])
    def heathcheck() -> Response:
        return make_response(jsonify({"message": "OK"}), 200)
