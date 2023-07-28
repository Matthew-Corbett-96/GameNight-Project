from flask import Flask, Response, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from ..models.models import db, User, Game, GameNight, GameNightGame, Attendance, Announcement
from uuid import UUID # used for generating unique ids

def setup_routes(app: Flask, api: Api) -> None:
    # Game model
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

        def post(self) -> Response:
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

        def put(self, game_id) -> Response:
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

        def delete(self, game_id) -> Response:
            game_id = UUID(game_id)
            game: Game = Game.query.filter_by(id=game_id).first()
            if game:
               db.session.delete(game)
               db.session.commit()
               return make_response(f"{game} was removed.", 200)
            
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
                password=data["password"]
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
                db.session.commit()
                return make_response(jsonify(user.to_dict()), 200)
            
            return make_response(jsonify({"message": "User not found."}), 404)
        
        def delete(self, user_id) -> Response:
            user_id: UUID = UUID(user_id)
            user: User = User.query.filter_by(id=user_id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return make_response(f"{user} was removed.", 200)
            
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
                return make_response(f"{game_night} was removed.", 200)
            
            return make_response(jsonify({"message": "Game night not found."}), 404)
        
    # GameNightGame model
    class GameNightGameRestClass(Resource):
        
        def get(self, game_night_game_id=None) -> Response:
            if game_night_game_id is None:
                game_night_games = GameNightGame.query.all()
                game_night_games_dict = [game_night_game.to_dict() for game_night_game in game_night_games]
                return make_response(jsonify(game_night_games_dict), 200)

            game_night_game_id: UUID = UUID(game_night_game_id)
            game_night_game: GameNightGame = GameNightGame.query.filter_by(id=game_night_game_id).first()
            if game_night_game:
                return make_response(jsonify(game_night_game.to_dict()), 200)
            
            return make_response(jsonify({"message": "Game night game not found."}), 404)
        
        def post(self) -> Response:
            data = request.json
            game_night_game: GameNightGame = GameNightGame(
                game_night_id=data["game_night_id"],
                game_id=data["game_id"]
            )
            db.session.add(game_night_game)
            db.session.commit()
            return make_response(jsonify(game_night_game.to_dict()), 200)
        
        def put(self, game_night_game_id) -> Response:
            game_night_game_id: UUID = UUID(game_night_game_id)
            data = request.json
            game_night_game: GameNightGame = GameNightGame.query.filter_by(id=game_night_game_id).first()
            if game_night_game:
                game_night_game.game_night_id = data["game_night_id"]
                game_night_game.game_id = data["game_id"]
                db.session.commit()
                return make_response(jsonify(game_night_game.to_dict()), 200)
            
            return make_response(jsonify({"message": "Game night game not found."}), 404)
        
        def delete(self, game_night_game_id) -> Response:
            game_night_game_id: UUID = UUID(game_night_game_id)
            game_night_game: GameNightGame = GameNightGame.query.filter_by(id=game_night_game_id).first()
            if game_night_game:
                db.session.delete(game_night_game)
                db.session.commit()
                return make_response(f"{game_night_game} was removed.", 200)
            
            return make_response(jsonify({"message": "Game night game not found."}), 404)


    # Attendance model
    class AttendanceRestClass(Resource):
        def get(self, attendance_id=None) -> Response:

            args: dict[str,str] = request.args
            user_id: str = args.get("user_id")
            game_night_id: str = args.get("game_night_id")

            # When an attendance_id is provided, return the attendance with that id
            if attendance_id is not None:
                attendance_id: UUID = UUID(attendance_id)
                attendance: Attendance = Attendance.query.filter_by(id=attendance_id).first()
                if attendance:
                    return make_response(jsonify(attendance.to_dict()), 200)
                
                return make_response(jsonify({"message": "Attendance not found."}), 404)
            
            # Filter attendances by user_id or game_night_id
            query = Attendance.query
            if user_id is not None:
                user_id: UUID = UUID(user_id)
                query = query.filter_by(user_id=user_id)
            if game_night_id is not None:
                game_night_id: UUID = UUID(game_night_id)
                query = query.filter_by(game_night_id=game_night_id)
            attendances = query.all()
            attendances_list: list = [attendance.to_dict() for attendance in attendances]
            return make_response(jsonify(attendances_list), 200)

        def post(self) -> Response:
            data = request.json
            attendance: Attendance = Attendance(
                user_id=data["user_id"],
                game_night_id=data["game_night_id"],
                status=data["status"]
            )
            db.session.add(attendance)
            db.session.commit()
            return make_response(jsonify(attendance.to_dict()), 200)
        
        def put(self, attendance_id) -> Response:
            attendance_id: UUID = UUID(attendance_id)
            data = request.json
            attendance: Attendance = Attendance.query.filter_by(id=attendance_id).first()
            if attendance:
                attendance.user_id = data["user_id"]
                attendance.game_night_id = data["game_night_id"]
                attendance.status = data["status"]
                db.session.commit()
                return make_response(jsonify(attendance.to_dict()), 200)
            
            return make_response(jsonify({"message": "Attendance not found."}), 404)
        
        def delete(self, attendance_id) -> Response:
            attendance_id: UUID = UUID(attendance_id)
            attendance: Attendance = Attendance.query.filter_by(id=attendance_id).first()
            if attendance:
                db.session.delete(attendance)
                db.session.commit()
                return make_response(f"{attendance} was removed.", 200)
            
            return make_response(jsonify({"message": "Attendance not found."}), 404)
        

    # Announcment model
    class AnnouncementRestClass(Resource):
        def get(self, announcement_id=None) -> Response:

            args = request.args
            active: bool = args.get("active")

            # When an announcement_id is provided, return the announcement with that id
            if announcement_id is not None:
                announcement_id: UUID = UUID(announcement_id)
                announcement: Announcement = Announcement.query.filter_by(id=announcement_id).first()
                if announcement:
                    return make_response(jsonify(announcement.to_dict()), 200)
                
                return make_response(jsonify({"message": "Announcement not found."}), 404)

            # Filter announcements by active if provided
            query = Announcement.query
            if active is not None:
                if active.lower() == "true":
                    active = True
                elif active.lower() == "false":
                    active = False
                else:
                    return make_response(jsonify({"message": "Invalid active value."}), 400)
                query = query.filter(Announcement.is_active == active)
            announcements = query.all()
            announcements_list = [announcement.to_dict() for announcement in announcements]
            return make_response(jsonify(announcements_list), 200)
        
        def post(self) -> Response:
            data = request.json
            announcement: Announcement = Announcement(
                user_id=data["user_id"],
                start_date=data["start_date"],
                end_date=data["end_date"],
                content=data["content"]
            )
            db.session.add(announcement)
            db.session.commit()
            return make_response(jsonify(announcement.to_dict()), 200)
        
        def put(self, announcement_id) -> Response:
            announcement_id: UUID = UUID(announcement_id)
            data = request.json
            announcement: Announcement = Announcement.query.filter_by(id=announcement_id).first()
            if announcement:
                announcement.user_id = data["user_id"]
                announcement.start_date = data["start_date"]
                announcement.end_date = data["end_date"]
                announcement.content = data["content"]
                db.session.commit()
                return make_response(jsonify(announcement.to_dict()), 200)
            
            return make_response(jsonify({"message": "Announcement not found."}), 404)
        
        def delete(self, announcement_id) -> Response:
            announcement_id: UUID = UUID(announcement_id)
            announcement: Announcement = Announcement.query.filter_by(id=announcement_id).first()
            if announcement:
                db.session.delete(announcement)
                db.session.commit()
                return make_response(f"{announcement} was removed.", 200)
            
            return make_response(jsonify({"message": "Announcement not found."}), 404)
        
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
    api.add_resource(AttendanceRestClass, 
                     "/attendances/", 
                     "/attendances/<string:attendance_id>", 
                     "/attendances/?user_id=<string:user_id>", 
                     "/attendances/?game_night_id=<string:game_night_id>"
                     )
    api.add_resource(AnnouncementRestClass, 
                     "/announcements/", 
                     "/announcements/<string:announcement_id>", 
                     "/announcements/?active=<string:active>"
                     )
    api.add_resource(GameNightGameRestClass,
                    "/game_night_games/",
                    "/game_night_games/<string:game_night_game_id>"
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
