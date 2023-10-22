import datetime
from flask import Flask, Response, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from ..models.models import db, User, Game, GameNight, Round, RSVPLog, Notification, UserRole
from uuid import UUID # used for generating unique ids
from .tools import Response200, Response400, Response401, Response404, Response500

def setup_routes(app: Flask, api: Api) -> None:
    # Game model
    class GameRestClass(Resource):
        def get(self, game_id = None) -> Response:
            if game_id is None:
                games_dict = [
                    game.to_dict() for game in Game.query.all()
                ]
                response = Response200(data={"Games": games_dict}).to_dict()
                return make_response(jsonify(response), 200)

            game: Game = Game.query.filter_by(id=game_id).first()
            if game is None:
                return make_response(jsonify(Response404('Game Not Found').to_dict()), 404)
            
            response = Response200(data={'Game': game.to_dict()}).to_dict()
            return make_response(jsonify(response), 200)

        def post(self) -> Response:
            data = request.json
            game: Game = Game(
                name=data.get("name"),
                description=data.get("description"),
                min_players=data.get("min_players"),
                max_players=data.get("max_players"),
            )
            db.session.add(game)
            db.session.commit()
            response = Response200(data=game.to_dict()).to_dict()
            return make_response(jsonify(response), 200)

        def put(self, game_id) -> Response:
            data = request.json
            game: Game = Game.query.filter_by(id=game_id).first()
            if game is None:
                return make_response(jsonify(Response404('Game Not Found').to_dict()), 404)
            
            game.name = data.get("name", game.name)
            game.description = data.get("description", game.description)
            game.min_players = data.get("min_players", game.min_players)
            game.max_players = data.get("max_players", game.max_players)
            db.session.commit()

            response = Response200(data={'Game': game.to_dict()}).to_dict()
            return make_response(jsonify(response), 200)

        def delete(self, game_id) -> Response:
            game: Game = Game.query.filter_by(id=game_id).first()
            if game is None:
                return make_response(jsonify(Response404('Game Not Found').to_dict()), 404)

            db.session.delete(game)
            db.session.commit()
            return make_response(Response200(f'{game_id} Deleted').to_dict(), 200)
    # User model
    class UserRestClass(Resource):
        def get(self, user_id=None) -> Response:
            if user_id is None:
                users_dict: list[dict] = [user.to_dict() for user in User.query.all()]
                response: dict = Response200(data={"Users": users_dict}).to_dict()
                return make_response(jsonify(response), 200)

            user: User = User.query.filter_by(id=user_id).first()
            if user is None:
                return make_response(jsonify(Response404('User Not Found').to_dict()), 404)
            
            response = Response200(data={'User': user.to_dict()}).to_dict()
            return make_response(jsonify(response), 200)
            
        def post(self) -> Response:
            data = request.json

            # Check if role exists so we can assign to user
            role = None
            if data.get("role", None) is not None:
                role: UserRole | None = UserRole.query.filter_by(role_name=data["role"]).first()
                if role is None:
                    return make_response(jsonify(Response401(message="Role Id Not Found").to_dict()), 404)
                
            user: User = User(
                auth0_id=data.get("auth0_id"),
                username=data.get("username"),
                first_name=data.get("first_name", None),
                last_name=data.get("last_name", None),
                gender=data.get("gender", None),
                email=data.get("email"),
                phone_number=data.get("phone_number", None),
                role_id= role.id if role is not None else None,
                is_active= data.get("is_active", True)
            )
            db.session.add(user)
            db.session.commit()
            response: Response200 = Response200(
                data= {
                    "User": user.to_dict(),
                }
            )
            return make_response(jsonify(response.to_dict()), 200)
        
        def put(self, user_id) -> Response:
            data = request.json

            # Check if user exists
            user: User = User.query.filter_by(id=user_id).first()
            if user is None:
                return make_response(jsonify(Response404('User Not Found').to_dict()), 404)

            # Check if role exists so we can assign to user
            if data.get("role", None) is not None:
                role: UserRole | None = UserRole.query.filter_by(role_name=data["role"]).first()
                if role is None:
                    return make_response(jsonify(Response400(message="Role Id Not Found").to_dict()), 400)
            
            user.username = data.get("username", user.username)
            user.first_name = data.get("first_name", user.first_name)
            user.last_name = data.get("last_name", user.last_name)
            user.gender = data.get("gender", user.gender)
            user.email = data.get("email", user.email)
            user.phone_number = data.get("phone_number", user.phone_number)
            user.role_id = role.id
            user.is_active = data.get("is_active", user.is_active)


            db.session.commit()
            response: Response200 = Response200(
                data= {
                    "User": user.to_dict(),
                }
            ).to_dict()
            return make_response(jsonify(response), 200)
                
        def delete(self, user_id) -> Response:
            user: User = User.query.filter_by(id=user_id).first()
            if user is None:
                return make_response(jsonify(Response404.to_dict()), 404)
            
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify(Response200(message=f'{user_id} Deleted.')), 200)

    # GameNight model START HERE MATTHEW JAMES 10/10/2021
    class GameNightRestClass(Resource):
        def get(self, game_night_id=None) -> Response:
            if game_night_id is None:
                game_nights = GameNight.query.all()
                game_nights_dict = [game_night.to_dict() for game_night in game_nights]
                return make_response(jsonify(game_nights_dict), 200)

            game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
            if game_night is None:
                return make_response(jsonify({"message": "Game night not found."}), 404)
                
            return make_response(jsonify(game_night.to_dict()), 200)
            
        def post(self) -> Response:
            data = request.json
            game_night: GameNight = GameNight(
                date=data["date"]
            )
            db.session.add(game_night)
            db.session.commit()
            return make_response(jsonify(game_night.to_dict()), 200)
        
        def put(self, game_night_id) -> Response:
            data = request.json

            game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
            if game_night is None:
                return make_response(jsonify({"message": "Game night not found."}), 404)
            
            game_night.date = data["date"]
            db.session.commit()
            return make_response(jsonify(game_night.to_dict()), 200)      
        
        def delete(self, game_night_id) -> Response:
            game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
            if game_night is None:
                return make_response(jsonify({"message": "Game night not found."}), 404)

            db.session.delete(game_night)
            db.session.commit()
            return make_response(f'{game_night_id} Deleted', 200)
            
    # Round model
    class RoundRestClass(Resource):
        def get(self, round_id=None) -> Response:
            if round_id is None:
                rounds = Round.query.all()
                results_dict = [round.to_dict() for round in rounds]
                return make_response(jsonify(results_dict), 200)

            round: Round = Round.query.filter_by(id=round_id).first()
            if round is None:
                return make_response(jsonify({"message": "Round not found."}), 404)
            
            return make_response(jsonify(round.to_dict()), 200)
            
        def post(self) -> Response:
            data = request.json

            game_night = GameNight.query.filter_by(id=data["game_night_id"]).first()
            if game_night is None:
                return make_response(jsonify({"message": "Game night not found."}), 404)
            
            game = Game.query.filter_by(name=data["game"]).first()
            if game is None:
                return make_response(jsonify({"message": "Game not found."}), 404)
            
            round: Round = Round(
                game_night_id=game_night.id,
                game_id=game.id
            )
            db.session.add(round)
            db.session.commit()
            return make_response(jsonify(round.to_dict()), 200)
        
        def put(self, round_id) -> Response:
            data = request.json

            round: Round = Round.query.filter_by(id=round_id).first()
            if round is None:
                return make_response(jsonify({"message": "Round not found."}), 404)

            round.game_night_id = data["game_night_id"]
            round.game_id = data["game_id"]
            db.session.commit()
            return make_response(jsonify(round.to_dict()), 200)
            
        def delete(self, round_id) -> Response:
            round: Round = Round.query.filter_by(id=round_id).first()
            if round is None:
                return make_response(jsonify({"message": "Round not found."}), 404)

            db.session.delete(round)
            db.session.commit()
            return make_response(f'{round_id} Deleted',  200)
            
    # RSVPLog model
    class RSVPLogRestClass(Resource):
        def get(self, id=None) -> Response:

            args: dict[str,str] = request.args
            user_id: str = args.get("user_id")
            game_night_id: str = args.get("game_night_id")

            # When an attendance_id is provided, return the attendance with that id
            if id is not None:
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

            user = User.query.filter_by(username=data["username"]).first()
            if user is None:
                return make_response(jsonify({"message": "User not found."}), 404)
            
            game_night = GameNight.query.filter_by(id=data["game_night_id"]).first()
            if game_night is None:
                return make_response(jsonify({"message": "Game night not found."}), 404)

            rsvpLog: RSVPLog = RSVPLog.query.filter_by(user_id=user.id, game_night_id=game_night.id).first()
            if rsvpLog:
                rsvpLog.response_status = data["response_status"]
                rsvpLog.response_date = datetime.datetime.now()
                db.session.commit()
                return make_response(jsonify(rsvpLog.to_dict()), 200)

            rsvp: RSVPLog = RSVPLog(
                user_id=user.id,
                game_night_id=game_night.id,
                response_status=data["response_status"]
            )
            db.session.add(rsvp)
            db.session.commit()
            return make_response(jsonify(rsvp.to_dict()), 200)
        
        def delete(self, id) -> Response:
            rsvp: RSVPLog = RSVPLog.query.filter_by(id=id).first()
            if rsvp:
                db.session.delete(rsvp)
                db.session.commit()
                return make_response(f'{id} Deleted', 200)
            
            return make_response(jsonify({"message": "Not found."}), 404)

    class NotificationRestClass(Resource):
        def get(self, notification_id=None) -> Response:
            if notification_id is None:
                notifications = Notification.query.all()
                notifications_dict = [notification.to_dict() for notification in notifications]
                return make_response(jsonify(notifications_dict), 200)

            notification: Notification = Notification.query.filter_by(id=notification_id).first()
            if notification is None:
                return make_response(jsonify({"message": "Notification not found."}), 404)
            
            return make_response(jsonify(notification.to_dict()), 200)
    
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
            if notification is None:
                return make_response(jsonify({"message": "Notification not found."}), 404)

            notification.message = data["message"]
            notification.start_date = data["start_date"]
            notification.end_date = data["end_date"]
            notification.channel = data["channel"]
            notification.notification_type = data["notification_type"]
            db.session.commit()
            return make_response(jsonify(notification.to_dict()), 200)
            
        def delete(self, notification_id) -> Response:

            notification: Notification = Notification.query.filter_by(id=notification_id).first()
            if notification is None:
                return make_response(jsonify({"message": "Notification not found."}), 404)

            db.session.delete(notification)
            db.session.commit()
            return make_response(f'{notification_id} Deleted', 200)
            
    class UserRoleRestClass(Resource):
        def get(self, role_id=None) -> Response:
            if role_id is None:
                roles = UserRole.query.all()
                roles_dict = [role.to_dict() for role in roles]
                return make_response(jsonify(roles_dict), 200)

            role: UserRole = UserRole.query.filter_by(id=role_id).first()
            if role is None:
                return make_response(jsonify({"message": "Role not found."}), 404)
            
            return make_response(jsonify(role.to_dict()), 200)
             
        def post(self) -> Response:
            data = request.json
            role: UserRole = UserRole(
                role_name=data["role"],
                permissions=data["permissions"]
            )
            db.session.add(role)
            db.session.commit()
            return make_response(jsonify(role.to_dict()), 200)
        
        def put(self, role_id) -> Response:
            data = request.json

            role: UserRole = UserRole.query.filter_by(id=role_id).first()
            if role is None:
                return make_response(jsonify({"message": "Role not found."}), 404)

            role.role_name = data["role"]
            role.permissions = data["permissions"]
            db.session.commit()
            return make_response(jsonify(role.to_dict()), 200)       
        
        def delete(self, role_id) -> Response:
            role: UserRole = UserRole.query.filter_by(id=role_id).first()
            if role is None:
                return make_response(jsonify({"message": "Role not found."}), 404)

            db.session.delete(role)
            db.session.commit()
            return make_response(f'{role_id} Deleted', 200)
            

    # Add resources to api
    api.add_resource(GameRestClass, 
                     "/games/", 
                     "/games/<uuid:game_id>"
                     )
    api.add_resource(UserRestClass, 
                     "/users/", 
                     "/users/<uuid:user_id>"
                     )
    api.add_resource(GameNightRestClass, 
                     "/gamenights/", 
                     "/gamenights/<uuid:game_night_id>"
                     )
    api.add_resource(RSVPLogRestClass, 
                     "/rsvps/", 
                     "/rsvps/<uuid:id>", 
                     "/rsvps/?user_id=<uuid:user_id>", 
                     "/rsvp/?game_night_id=<uuid:game_night_id>"
                     )
    api.add_resource(RoundRestClass,
                    "/rounds/",
                    "/rounds/<uuid:round_id>"
                    )
    api.add_resource(NotificationRestClass,
                    "/notifications/",
                    "/notifications/<uuid:notification_id>"
                    )
    api.add_resource(UserRoleRestClass,
                    "/roles/",
                    "/roles/<uuid:role_id>"
                    )

    # Healthcheck
    @app.route("/healthcheck", methods=["GET"])
    def heathcheck() -> Response:
        return make_response(jsonify(Response200.to_dict()), 200)
    
    # 404
    @app.errorhandler(404)
    def not_found(error) -> Response:
        return make_response(jsonify(Response404('Path Not Found').to_dict()), 404)
    
    # 500
    @app.errorhandler(500)
    def internal_server_error(error) -> Response:
        return make_response(jsonify(Response500.to_dict()), 500)
    
    # 400
    @app.errorhandler(400)
    def bad_request(error) -> Response:
        return make_response(jsonify(Response400.to_dict()), 400)
    