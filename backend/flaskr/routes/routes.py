from flask import Flask, Response, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from ..models.models import db, User, Game, GameNight, Round, RSVPLog, Notification
from uuid import UUID # used for generating unique ids

def setup_routes(app: Flask, api: Api) -> None:
    # Game model
    class GameRestClass(Resource):
        def get(self, game_id: str = None) -> Response:
            if game_id is None:
                games = Game.query.all()
                games_dict = [
                    game.to_dict() for game in games   
                ]
                return make_response(jsonify(games_dict), 200)

            game_id_uuid = UUID(game_id)
            game: Game = Game.query.filter_by(id=game_id_uuid).first()
            if game:
                return make_response(jsonify(game.to_dict()), 200)
            
            return make_response(jsonify({"message": "Game not found."}), 404)

        def post(self) -> Response:
            data = request.json
            game: Game = Game(
                name=data["name"],
                description=data["description"],
                min_players=data["min_players"],
                max_players=data["max_players"],
            )
            db.session.add(game)
            db.session.commit()
            return make_response(jsonify(game.to_dict()), 200)

        def put(self, game_id) -> Response:
            game_id = UUID(game_id)
            data = request.json
            game: Game = Game.query.filter_by(id=game_id).first()
            if game:
                game.name = data["name"]
                game.description = data["description"]
                game.min_players = data["min_players"]
                game.max_players = data["max_players"]
                db.session.commit()
                return make_response(jsonify(game.to_dict()), 200)
            
            return make_response(jsonify({"message": "Game not found."}), 404)

        def delete(self, game_id) -> Response:
            game_id = UUID(game_id)
            game: Game = Game.query.filter_by(id=game_id).first()
            if game:
               db.session.delete(game)
               db.session.commit()
               return make_response(200)
            
            return make_response(jsonify({"message": "Game not found."}), 404)

    # User model
    class UserRestClass(Resource):
        def get(self, user_id=None) -> Response:
            if user_id is None:
                users = User.query.all()
                users_dict = [user.to_dict() for user in users]
                return make_response(jsonify(users_dict), 200)

            user_id: UUID = UUID(user_id)
            user: User = User.query.filter_by(id=user_id).first()
            if user:
               return make_response(jsonify(user.to_dict()), 200)
            
            return make_response(jsonify({"message": "User not found."}), 404)
        
        def post(self) -> Response:
            data = request.json
            user: User = User(
                username=data["username"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                gender=["gender"],
                email=data["email"],
                phone_number=data["phone_number"],
                password=data["password"],
                role_id=data["role_id"],
                is_active=data["is_active"]
            )
            db.session.add(user)
            db.session.commit()
            return make_response(jsonify(user.to_dict()), 200)
        
        def put(self, user_id) -> Response:
            user_id: UUID = UUID(user_id)
            data = request.json
            user: User = User.query.filter_by(id=user_id).first()
            if user:
                user.username = data["username"]
                user.first_name = data["first_name"]
                user.last_name = data["last_name"]
                user.gender = data["gender"]
                user.email = data["email"]
                user.phone_number = data["phone_number"]
                user.password = data["password"]
                user.role_id = data["role_id"]
                user.is_active = data["is_active"]
                db.session.commit()
                return make_response(jsonify(user.to_dict()), 200)
            
            return make_response(jsonify({"message": "User not found."}), 404)
        
        def delete(self, user_id) -> Response:
            user_id: UUID = UUID(user_id)
            user: User = User.query.filter_by(id=user_id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return make_response(200)
            
            return make_response(jsonify({"message": "User not found."}), 404)

    # GameNight model
    class GameNightRestClass(Resource):
        def get(self, game_night_id=None) -> Response:
            if game_night_id is None:
                game_nights = GameNight.query.all()
                game_nights_dict = [game_night.to_dict() for game_night in game_nights]
                return make_response(jsonify(game_nights_dict), 200)

            game_night_id: UUID = UUID(game_night_id)
            game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
            if game_night:
                return make_response(jsonify(game_night.to_dict()), 200)
            
            return make_response(jsonify({"message": "Game night not found."}), 404)
        
        def post(self) -> Response:
            data = request.json
            game_night: GameNight = GameNight(
                date=data["date"]
            )
            db.session.add(game_night)
            db.session.commit()
            return make_response(jsonify(game_night.to_dict()), 200)
        
        def put(self, game_night_id) -> Response:
            game_night_id: UUID = UUID(game_night_id)
            data = request.json
            game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
            if game_night:
                game_night.date = data["date"]
                db.session.commit()
                return make_response(jsonify(game_night.to_dict()), 200)
            
            return make_response(jsonify({"message": "Game night not found."}), 404)
        
        def delete(self, game_night_id) -> Response:
            game_night_id: UUID = UUID(game_night_id)
            game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
            if game_night:
                db.session.delete(game_night)
                db.session.commit()
                return make_response(200)
            
            return make_response(jsonify({"message": "Game night not found."}), 404)
        
    # GamesPlayed model
    class RoundRestClass(Resource):
        
        def get(self, round_id=None) -> Response:
            if round_id is None:
                rounds = Round.query.all()
                results_dict = [round.to_dict() for round in rounds]
                return make_response(jsonify(results_dict), 200)

            round_id: UUID = UUID(round_id)
            round: Round = Round.query.filter_by(id=round_id).first()
            if round:
                return make_response(jsonify(round.to_dict()), 200)
            
            return make_response(jsonify({"message": "Round not found."}), 404)
        
        def post(self) -> Response:
            data = request.json
            round: Round = Round(
                game_night_id=data["game_night_id"],
                game_id=data["game_id"]
            )
            db.session.add(round)
            db.session.commit()
            return make_response(jsonify(round.to_dict()), 200)
        
        def put(self, round_id) -> Response:
            round_id: UUID = UUID(round_id)
            data = request.json
            round: Round = Round.query.filter_by(id=round_id).first()
            if round:
                round.game_night_id = data["game_night_id"]
                round.game_id = data["game_id"]
                db.session.commit()
                return make_response(jsonify(round.to_dict()), 200)
            
            return make_response(jsonify({"message": "Round not found."}), 404)
        
        def delete(self, round_id) -> Response:
            round_id: UUID = UUID(round_id)
            round: Round = Round.query.filter_by(id=round_id).first()
            if round:
                db.session.delete(round)
                db.session.commit()
                return make_response(200)
            
            return make_response(jsonify({"message": "Round not found."}), 404)


    # RSVPLog model
    class RSVPLogRestClass(Resource):
        def get(self, id=None) -> Response:

            args: dict[str,str] = request.args
            user_id: str = args.get("user_id")
            game_night_id: str = args.get("game_night_id")

            # When an attendance_id is provided, return the attendance with that id
            if id is not None:
                id: UUID = UUID(id)
                rsvp: RSVPLog = RSVPLog.query.filter_by(id=id).first()
                if rsvp:
                    return make_response(jsonify(rsvp.to_dict()), 200)
                
                return make_response(jsonify({"message": "RSVP not found."}), 404)
            
            # Filter attendances by user_id or game_night_id
            query = RSVPLog.query
            if user_id is not None:
                user_id: UUID = UUID(user_id)
                query = query.filter_by(user_id=user_id)
            if game_night_id is not None:
                game_night_id: UUID = UUID(game_night_id)
                query = query.filter_by(game_night_id=game_night_id)
            rsvps = query.all()
            results: list = [rsvp.to_dict() for rsvp in rsvps]
            return make_response(jsonify(results), 200)

        def post(self) -> Response:
            data = request.json
            rsvp: RSVPLog = RSVPLog(
                user_id=data["user_id"],
                game_night_id=data["game_night_id"],
                status=data["status"]
            )

            rsvpLog: RSVPLog = RSVPLog.query.filter_by(user_id=data["user_id"], game_night_id=data["game_night_id"]).first()
            if rsvpLog:
                rsvpLog.status = data["status"]
                db.session.commit()
                return make_response(jsonify(rsvpLog.to_dict()), 200)

            db.session.add(rsvp)
            db.session.commit()
            return make_response(jsonify(rsvp.to_dict()), 200)
        
        def delete(self, id) -> Response:
            id: UUID = UUID(id)
            rsvp: RSVPLog = RSVPLog.query.filter_by(id=id).first()
            if rsvp:
                db.session.delete(rsvp)
                db.session.commit()
                return make_response(200)
            
            return make_response(jsonify({"message": "Not found."}), 404)

    class NotificationRestClass(Resource):

        def get(self, notification_id=None) -> Response:
            if notification_id is None:
                notifications = Notification.query.all()
                notifications_dict = [notification.to_dict() for notification in notifications]
                return make_response(jsonify(notifications_dict), 200)

            notification_id: UUID = UUID(notification_id)
            notification: Notification = Notification.query.filter_by(id=notification_id).first()
            if notification:
                return make_response(jsonify(notification.to_dict()), 200)
            
            return make_response(jsonify({"message": "Notification not found."}), 404)
    
        def post(self) -> Response:
            data = request.json
            notification: Notification = Notification(
                message=data["message"],
                start_date=data["start_date"],
                end_date=data["end_date"],
                channel=data["channel"],
                notification_type=data["notification_type"]
            )
            db.session.add(notification)
            db.session.commit()
            return make_response(jsonify(notification.to_dict()), 200)
    
        def put(self, notification_id) -> Response:
            data = request.json
            notification: Notification = Notification.query.filter_by(id=notification_id).first()
            if notification:
                notification.message = data["message"]
                notification.start_date = data["start_date"]
                notification.end_date = data["end_date"]
                notification.channel = data["channel"]
                notification.notification_type = data["notification_type"]
                db.session.commit()
                return make_response(jsonify(notification.to_dict()), 200)
            
            return make_response(jsonify({"message": "Notification not found."}), 404)
    
        def delete(self, notification_id) -> Response:
            notification: Notification = Notification.query.filter_by(id=notification_id).first()
            if notification:
                db.session.delete(notification)
                db.session.commit()
                return make_response(200)
            
            return make_response(jsonify({"message": "Notification not found."}), 404)
        
    # Add resources to api
    api.add_resource(GameRestClass, 
                     "/games/", 
                     "/games/<string:game_id>"
                     )
    api.add_resource(UserRestClass, 
                     "/users/", 
                     "/users/<string:user_id>"
                     )
    api.add_resource(GameNightRestClass, 
                     "/game_nights/", 
                     "/game_nights/<string:game_night_id>"
                     )
    api.add_resource(RSVPLogRestClass, 
                     "/rsvps/", 
                     "/rsvps/<string:rsvp_id>", 
                     "/rsvps/?user_id=<string:user_id>", 
                     "/rsvp/?game_night_id=<string:game_night_id>"
                     )
    api.add_resource(RoundRestClass,
                    "/rounds/",
                    "/rounds/<string:round_id>"
                    )
    api.add_resource(NotificationRestClass,
                    "/notifications/",
                    "/notifications/<uuid:notification_id>"
                    )

    # Healthcheck
    @app.route("/healthcheck", methods=["GET"])
    def heathcheck() -> Response:
        return make_response(jsonify({"message": "OK"}), 200)
    
    # 404
    @app.errorhandler(404)
    def not_found(error) -> Response:
        return make_response(jsonify({"error": "Not found"}), 404)
    
    # 500
    @app.errorhandler(500)
    def internal_server_error(error) -> Response:
        return make_response(jsonify({"error": "Internal server error"}), 500)
    
    # 400
    @app.errorhandler(400)
    def bad_request(error) -> Response:
        return make_response(jsonify({"error": "Bad request"}), 400)
    
    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #
