from flask import Response, request
from flask_restful import Resource, Api
from ..models.models import db, Notification
from .response import Response200, Response404, send_json_response

class NotificationRestClass(Resource):
    def get(self, notification_id=None) -> Response:
        if notification_id is None:
            notifications_dict = [
                notification.to_dict() for notification in Notification.query.all()
            ]
            return send_json_response(
                Response200(data={"notifications": notifications_dict})
            )

        notification: Notification = Notification.query.filter_by(
            id=notification_id
        ).first()
        if notification is None:
            return send_json_response(Response404("Notification Not Found"))

        return send_json_response(
            Response200(data={"notification": notification.to_dict()})
        )

    def post(self) -> Response:
        data = request.json
        notification: Notification = Notification(
            message=data.get("message", None),
            start_date=data.get("start_date", None),
            end_date=data.get("end_date", None),
            channel=data.get("channel", None),
            notification_type=data.get("notification_type", None),
        )
        db.session.add(notification)
        db.session.commit()
        return send_json_response(
            Response200(data={"notification": notification.to_dict()})
        )

    def put(self, notification_id) -> Response:
        data = request.json

        # Check if notification exists
        notification: Notification = Notification.query.filter_by(
            id=notification_id
        ).first()
        if notification is None:
            return send_json_response(Response404("Notification Not Found"))

        # Update notification
        notification.message = data.get("message", notification.message)
        notification.start_date = data.get("start_date", notification.start_date)
        notification.end_date = data.get("end_date", notification.end_date)
        notification.channel = data.get("channel", notification.channel)
        notification.notification_type = data.get(
            "notification_type", notification.notification_type
        )
        db.session.commit()
        return send_json_response(
            Response200(data={"notification": notification.to_dict()})
        )

    def delete(self, notification_id) -> Response:
        # Check if notification exists
        notification: Notification = Notification.query.filter_by(
            id=notification_id
        ).first()
        if notification is None:
            return send_json_response(Response404("Notification Not Found"))

        # Delete notification
        db.session.delete(notification)
        db.session.commit()
        return send_json_response(Response200(f"{notification_id} Deleted"))


def setup_routes_for_notification(api: Api) -> None:
    api.add_resource(
        NotificationRestClass,
        "/notifications/",
        "/notifications/<uuid:notification_id>",
    )
