import datetime
from flask import Response, request
from flask_restful import Resource, Api
from ..models.models import db, User, GameNight, RSVPLog
from uuid import UUID # used for generating unique ids
from .response import Response200, Response400, Response404, send_json_response

# RSVPLog model
class RSVPLogRestClass(Resource):
    def get(self, id=None) -> Response:
        args: dict[str, str] = request.args
        user_id: UUID = args.get("user_id")
        game_night_id: UUID = args.get("game_night_id")

        # When an attendance_id is provided, return the attendance with that id
        if id is not None:
            rsvp: RSVPLog = RSVPLog.query.filter_by(id=id).first()
            if rsvp is None:
                return send_json_response(Response404("RSVP Not Found"))

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
            return send_json_response(Response404("User Not Found"))

        # Check if game night exists
        game_night = GameNight.query.filter_by(id=data["game_night_id"]).first()
        if game_night is None:
            return send_json_response(Response404("Game Night Not Found"))

        # Validate Response Status as YES, NO, or MAYBE
        if data.get("response_status", None) not in ["YES", "NO", "MAYBE"]:
            return send_json_response(
                Response400("Response Status Must Be YES, NO, or MAYBE")
            )

        # Check if user has already RSVP'd
        rsvpLog: RSVPLog = RSVPLog.query.filter_by(
            user_id=user.id, game_night_id=game_night.id
        ).first()
        if rsvpLog:
            rsvpLog.response_status = data.get(
                "response_status", rsvpLog.response_status
            )
            rsvpLog.response_date = datetime.datetime.now()
            db.session.commit()
            return send_json_response(Response200(data={"rsvp": rsvpLog.to_dict()}))

        rsvp: RSVPLog = RSVPLog(
            user_id=user.id,
            game_night_id=game_night.id,
            response_status=data.get("response_status"),
        )
        db.session.add(rsvp)
        db.session.commit()
        return send_json_response(Response200(data={"rsvp": rsvp.to_dict()}))

    def delete(self, id) -> Response:
        rsvp: RSVPLog = RSVPLog.query.filter_by(id=id).first()
        if rsvp is None:
            return send_json_response(Response404("RSVP Not Found"))

        db.session.delete(rsvp)
        db.session.commit()
        return send_json_response(Response200(f"{id} Deleted"))


def setup_routes_for_rsvp_log(api: Api) -> None:
    api.add_resource(
        RSVPLogRestClass,
        "/rsvps/",
        "/rsvps/<uuid:id>",
        "/rsvps/?user_id=<uuid:user_id>",
        "/rsvp/?game_night_id=<uuid:game_night_id>",
    )
