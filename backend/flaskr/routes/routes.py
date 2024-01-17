import datetime
from flask import Flask, Response, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from ..models.models import db, User, Game, GameNight, Round, RSVPLog, Notification, UserRole
from uuid import UUID # used for generating unique ids
from .tools import Response200, Response400, Response401, Response404, Response500, CustomResponse, Response201

def setup_routes(app: Flask, api: Api) -> None:
    # Game model
    class GameRestClass(Resource):
        def get(self, game_id = None) -> Response:
            if game_id is None:
                games_dict = [game.to_dict() for game in Game.query.all()]
                return send_json_response(Response200(data={"games": games_dict}))

            game: Game = Game.query.filter_by(id=game_id).first()
            if game is None:
                return send_json_response(Response404('Game Not Found'))
            
            return send_json_response(Response200(data={"game" : game.to_dict()}))

        def post(self) -> Response:
            data = request.json
            print(data)

            # Check if game name is already taken
            if Game.query.filter_by(name=data["name"]).first() is not None:
                return send_json_response(Response401(message=f"Game Name '{data.get('name')}' Already Exists"))

            game: Game = Game(
                name=data.get("name"),
                description=data.get("description"),
                min_players=data.get("min_players"),
                max_players=data.get("max_players"),
            )
            db.session.add(game)
            db.session.commit()
            return send_json_response(Response200(data={"game" : game.to_dict()}))

        def put(self, game_id) -> Response:
            data = request.json
            # Check if game exists
            game: Game = Game.query.filter_by(id=game_id).first()
            if game is None:
                return send_json_response(Response404('Game Not Found'))
            
            # Check if game name is already taken
            if data.get("name", None) is not None:
                if data["name"] != game.name:
                    if Game.query.filter_by(name=data["name"]).first() is not None:
                        return send_json_response(Response401(message=f"Game Name '{data.get('name')}' Already Exists"))
            
            game.name = data.get("name", game.name)
            game.description = data.get("description", game.description)
            game.min_players = data.get("min_players", game.min_players)
            game.max_players = data.get("max_players", game.max_players)
            db.session.commit()


            return send_json_response(Response200(data={"game" : game.to_dict()}))

        def delete(self, game_id) -> Response:
            game: Game = Game.query.filter_by(id=game_id).first()
            if game is None:
                return send_json_response(Response404('Game Not Found'))

            db.session.delete(game)
            db.session.commit()
            return send_json_response(Response200(f'{game_id} Deleted'))
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
            
            # Check if email exists already
            if User.query.filter_by(email=data["email"]).first() is not None:
                return send_json_response(Response400(message=f"Email '{data.get('email')}' Already Exists"))

            # Check if username exists already
            if User.query.filter_by(username=data["username"]).first() is not None:
                return send_json_response(Response400(message=f"Username '{data.get('username')}' Already Exists"))
            
            # Check if auth0_id exists already
            if User.query.filter_by(auth0_id=data["auth0_id"]).first() is not None:
                return send_json_response(Response400(message=f"Auth0 Id '{data.get('auth0_id')}' Already Exists"))

            # Check if role exists so we can assign to user
            role = None
            if data.get("role", None) is not None:
                role: UserRole = UserRole.query.filter_by(role_name=data["role"]).first()
                if role is None:
                    return send_json_response(Response400(message=f"Role'{data.get('role')}' Not Found"))
                
            phone = None
            if data.get("phone_number", None) is not None:
                phone: str = data["phone_number"]
                if User.query.filter_by(phone_number=phone).first() is not None:
                    return send_json_response(Response400(message=f"Phone Number '{data.get('phone_number')}' Already Exists")) 
                 
            user: User = User(
                auth0_id=data.get("auth0_id"),
                username=data.get("username"),
                first_name=data.get("first_name", None),
                last_name=data.get("last_name", None),
                gender=data.get("gender", None),
                email=data.get("email"),
                phone_number= phone if phone is not None else None,
                role_id= role.id if role is not None else None,
                is_active= data.get("is_active", True)
            )
            db.session.add(user)
            db.session.commit()
    
            return send_json_response(Response201(data={"User": user.to_dict()}))
        
        def put(self, user_id) -> Response:
            data = request.json

            # Check if user exists
            user: User = User.query.filter_by(id=user_id).first()
            if user is None:
                return send_json_response(Response404('User Not Found'))

            # if username --> Check if username is already taken
            if data.get("username", None) is not None:
                if data["username"] != user.username:
                    if User.query.filter_by(username=data["username"]).first() is not None:
                        return send_json_response(Response400(message=f"Username '{data.get('username')}' Already Exists"))
            
            # if email --> Check if email is already taken
            if data.get("email", None) is not None:
                if data["email"] != user.email:
                    if User.query.filter_by(email=data["email"]).first() is not None:
                        return send_json_response(Response400(message=f"Email '{data.get('email')}' Already Exists"))
            
            # if auth0_id --> Check if auth0_id is already taken
            if data.get("auth0_id", None) is not None:
                if data["auth0_id"] != user.auth0_id:
                    if User.query.filter_by(auth0_id=data["auth0_id"]).first() is not None:
                        return send_json_response(Response400(message=f"Auth0 Id '{data.get('auth0_id')}' Already Exists"))

            # if role --> Check if role exists so we can assign to user
            role = None
            if data.get("role", None) is not None:
                role: UserRole = UserRole.query.filter_by(role_name=data["role"]).first()
                if role is None:
                    return send_json_response(Response400(message=f"Role'{data.get('role')}' Not Found"))
            
            # if phone_number --> Check if phone_number is already taken
            if data.get("phone_number", None) is not None:
                if User.query.filter_by(phone_number=data["phone_number"]).first() is not None:
                    return send_json_response(Response400(message=f"Phone Number '{data.get('phone_number')}' Already Exists")) 

            user.username = data.get("username", user.username)
            user.auth0_id = data.get("auth0_id", user.auth0_id)
            user.first_name = data.get("first_name", user.first_name)
            user.last_name = data.get("last_name", user.last_name)
            user.gender = data.get("gender", user.gender)
            user.email = data.get("email", user.email)
            user.phone_number = data.get("phone_number", user.phone_number)
            user.role_id = role.id if role is not None else user.role_id
            user.is_active = data.get("is_active", user.is_active)

            db.session.commit()
            return send_json_response(Response200(data={"User": user.to_dict()}))
                
        def delete(self, user_id) -> Response:
            user: User = User.query.filter_by(id=user_id).first()
            if user is None:
                return send_json_response(Response404('User Not Found'))
            
            db.session.delete(user)
            db.session.commit()
            return send_json_response(Response200(f'{user_id} Deleted'))

    # GameNight model
    class GameNightRestClass(Resource):
        def get(self, game_night_id=None) -> Response:
            if game_night_id is None:
                game_nights_dict = [game_night.to_dict() for game_night in GameNight.query.all()]
                return send_json_response(Response200(data={"game_nights": game_nights_dict}))

            game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
            if game_night is None:
                return send_json_response(Response404('Game Night Not Found'))
                
            return send_json_response(Response200(data={"game_night": game_night.to_dict()}))
            
        def post(self) -> Response:
            data = request.json
            game_night: GameNight = GameNight(
                date=data["date"]
            )
            db.session.add(game_night)
            db.session.commit()
            return send_json_response(Response200(data={"game_night": game_night.to_dict()}))
        
        def put(self, game_night_id) -> Response:
            data = request.json

            game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
            if game_night is None:
                return send_json_response(Response404('Game Night Not Found'))
            
            game_night.date = data["date"]
            db.session.commit()
            return send_json_response(Response200(data={"game_night": game_night.to_dict()}))   
        
        def delete(self, game_night_id) -> Response:
            game_night: GameNight = GameNight.query.filter_by(id=game_night_id).first()
            if game_night is None:
                return send_json_response(Response404('Game Night Not Found'))

            db.session.delete(game_night)
            db.session.commit()
            return send_json_response(Response200(f'{game_night_id} Deleted'))
            
    # Round model
    class RoundRestClass(Resource):
        def get(self, round_id=None) -> Response:
            if round_id is None:
                results_dict = [round.to_dict() for round in Round.query.all()]
                return send_json_response(Response200(data={"rounds": results_dict}))

            round: Round = Round.query.filter_by(id=round_id).first()
            if round is None:
                return send_json_response(Response404('Round Not Found'))
            
            return send_json_response(Response200(data={"round": round.to_dict()}))
            
        def post(self) -> Response:
            data = request.json

            game_night = GameNight.query.filter_by(id=data["game_night_id"]).first()
            if game_night is None:
                return send_json_response(Response404('Game Night Not Found'))
            
            game = Game.query.filter_by(name=data["game"]).first()
            if game is None:
                return send_json_response(Response404('Game Not Found'))
            
            round: Round = Round(
                game_night_id=game_night.id,
                game_id=game.id
            )
            db.session.add(round)
            db.session.commit()
            return send_json_response(Response200(data={"round": round.to_dict()}))
        
        def put(self, round_id) -> Response:
            data = request.json

            round: Round = Round.query.filter_by(id=round_id).first()
            if round is None:
                return send_json_response(Response404('Round Not Found'))

            round.game_night_id = data.get("game_night_id", round.game_night_id)
            round.game_id = data.get("game_id", round.game_id)
            db.session.commit()
            return send_json_response(Response200(data={"round": round.to_dict()}))
            
        def delete(self, round_id) -> Response:
            round: Round = Round.query.filter_by(id=round_id).first()
            if round is None:
                return send_json_response(Response404('Round Not Found'))

            db.session.delete(round)
            db.session.commit()
            return send_json_response(Response200(f'{round_id} Deleted'))
            
    # RSVPLog model
    class RSVPLogRestClass(Resource):
        def get(self, id=None) -> Response:

            args: dict[str,str] = request.args
            user_id: UUID = args.get("user_id")
            game_night_id: UUID = args.get("game_night_id")

            # When an attendance_id is provided, return the attendance with that id
            if id is not None:
                rsvp: RSVPLog = RSVPLog.query.filter_by(id=id).first()
                if rsvp is None:
                    return send_json_response(Response404('RSVP Not Found'))
                
                return send_json_response(Response200(data={"rsvp": rsvp.to_dict()}))
            
            # Filter attendances by user_id or game_night_id
            query = RSVPLog.query
            if user_id is not None:
                query = query.filter_by(user_id=user_id)
            if game_night_id is not None:
                query = query.filter_by(game_night_id=game_night_id)
            results: list = [rsvp.to_dict() for rsvp in query.all()]
            return send_json_response(Response200(data={"rsvps": results}))

        def post(self) -> Response:
            data = request.json

            # Check if user exists
            user = User.query.filter_by(username=data["username"]).first()
            if user is None:
                return send_json_response(Response404('User Not Found'))
            
            # Check if game night exists
            game_night = GameNight.query.filter_by(id=data["game_night_id"]).first()
            if game_night is None:
                return send_json_response(Response404('Game Night Not Found'))
            
            # Validate Response Status as YES, NO, or MAYBE
            if data.get("response_status", None) not in ["YES", "NO", "MAYBE"]:
                return send_json_response(Response400('Response Status Must Be YES, NO, or MAYBE'))

            # Check if user has already RSVP'd
            rsvpLog: RSVPLog = RSVPLog.query.filter_by(user_id=user.id, game_night_id=game_night.id).first()
            if rsvpLog:
                rsvpLog.response_status = data.get("response_status", rsvpLog.response_status)
                rsvpLog.response_date = datetime.datetime.now()
                db.session.commit()
                return send_json_response(Response200(data={"rsvp": rsvpLog.to_dict()}))

            rsvp: RSVPLog = RSVPLog(
                user_id=user.id,
                game_night_id=game_night.id,
                response_status= data.get('response_status')
            )
            db.session.add(rsvp)
            db.session.commit()
            return send_json_response(Response200(data={"rsvp": rsvp.to_dict()}))
        
        def delete(self, id) -> Response:
            rsvp: RSVPLog = RSVPLog.query.filter_by(id=id).first()
            if rsvp is None:
                return send_json_response(Response404('RSVP Not Found'))
            
            db.session.delete(rsvp)
            db.session.commit()
            return send_json_response(Response200(f'{id} Deleted'))

    class NotificationRestClass(Resource):
        def get(self, notification_id=None) -> Response:
            if notification_id is None:
                notifications_dict = [notification.to_dict() for notification in Notification.query.all()]
                return send_json_response(Response200(data={"notifications": notifications_dict}))

            notification: Notification = Notification.query.filter_by(id=notification_id).first()
            if notification is None:
                return send_json_response(Response404('Notification Not Found'))
            
            return send_json_response(Response200(data={"notification" : notification.to_dict()}))
    
        def post(self) -> Response:
            data = request.json
            notification: Notification = Notification(
                message= data.get("message", None),
                start_date= data.get("start_date", None),
                end_date= data.get("end_date", None),
                channel= data.get("channel", None),
                notification_type= data.get("notification_type", None)
            )
            db.session.add(notification)
            db.session.commit()
            return send_json_response(Response200(data={"notification" : notification.to_dict()}))
    
        def put(self, notification_id) -> Response:
            data = request.json

            # Check if notification exists
            notification: Notification = Notification.query.filter_by(id=notification_id).first()
            if notification is None:
                return send_json_response(Response404('Notification Not Found'))

            # Update notification
            notification.message = data.get("message", notification.message)
            notification.start_date = data.get("start_date", notification.start_date)
            notification.end_date = data.get("end_date", notification.end_date)
            notification.channel = data.get("channel", notification.channel)
            notification.notification_type = data.get("notification_type", notification.notification_type)
            db.session.commit()
            return send_json_response(Response200(data={"notification" : notification.to_dict()}))
            
        def delete(self, notification_id) -> Response:

            # Check if notification exists
            notification: Notification = Notification.query.filter_by(id=notification_id).first()
            if notification is None:
                return send_json_response(Response404('Notification Not Found'))

            # Delete notification
            db.session.delete(notification)
            db.session.commit()
            return send_json_response(Response200(f'{notification_id} Deleted'))
            
    class UserRoleRestClass(Resource):
        def get(self, role_id=None) -> Response:
            if role_id is None:
                roles_dict = [role.to_dict() for role in UserRole.query.all()]
                return send_json_response(Response200(data={"roles": roles_dict}))

            role: UserRole = UserRole.query.filter_by(id=role_id).first()
            if role is None:
                return send_json_response(Response404('Role Not Found'))
            
            return send_json_response(Response200(data={"role" : role.to_dict()}))
             
        def post(self) -> Response:
            data = request.json

            # Check if role exists already
            role: UserRole = UserRole.query.filter_by(role_name=data["role_name"]).first()
            if role is not None:
                return send_json_response(Response400('Role Already Exists'))
            
            # Create role
            role: UserRole = UserRole(
                role_name = data.get("role_name"),
                permissions = data.get("permissions")
            )
            db.session.add(role)
            db.session.commit()
            return send_json_response(Response200(data={"role" : role.to_dict()}))
        
        def put(self, role_id) -> Response:
            data = request.json

            # Check if role exists
            role: UserRole = UserRole.query.filter_by(id=role_id).first()
            if role is None:
                return send_json_response(Response404('Role Not Found'))
            
            # Check if new name is already taken
            if data.get("role_name", None) is not None:
                role: UserRole = UserRole.query.filter_by(role_name=data.get("role_name")).first()
                if role is not None:
                    return send_json_response(Response400(f"Role Name '{data.get('role_name')}' Already Exists"))

            # Update role
            role.role_name = data.get("role", role.role_name)
            role.permissions = data.get("permissions", role.permissions)
            db.session.commit()
            return send_json_response(Response200(data={"role" : role.to_dict()}))      
        
        def delete(self, role_id) -> Response:
            # Check if role exists
            role: UserRole = UserRole.query.filter_by(id=role_id).first()
            if role is None:
                return send_json_response(Response404('Role Not Found'))

            # Delete role
            db.session.delete(role)
            db.session.commit()
            return send_json_response(Response200(f'{role_id} Deleted'))
            
    class UserAuth0Class(Resource):
        def get(self, auth0_id: str) -> Response:
            user: User = User.query.filter_by(auth0_id=auth0_id).first()
            if user is None:
                return send_json_response(Response404('User Not Found'))
            
            return send_json_response(Response200(data={"user" : user.to_dict()}))

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
    api.add_resource(UserAuth0Class,
                    "/auth0/users/<string:auth0_id>"
                    )


    # Healthcheck
    @app.route("/healthcheck", methods=["GET"])
    def heathcheck() -> Response:
        return send_json_response(Response200("Healthy"))
    
    # 404
    @app.errorhandler(404)
    def not_found(error) -> Response:
        return send_json_response(Response404('Page Not Found'))
    
    # 500
    @app.errorhandler(500)
    def internal_server_error(error) -> Response:
        return send_json_response(Response500())
    
    # 400
    @app.errorhandler(400)
    def bad_request(error) -> Response:
        return send_json_response(Response400())
    
    
    @api.representation("application/json")
    def send_json_response(data: CustomResponse, headers=None):
        resp = make_response(jsonify(data.to_dict()), data.status)
        resp.headers.extend(headers or {})
        return resp
        
        
        