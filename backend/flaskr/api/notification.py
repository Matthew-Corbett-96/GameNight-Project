from flask import Response, request
from flask_restful import Resource, Api
from ..service.messageService import MessageService
from ..models.models import db, Notification
from .response import (
    Response200,
    Response404,
    send_json_response,
    Response400,
    Response500,
)
from twilio.base.exceptions import TwilioRestException


class NotificationRestClass(Resource):
    def get(self, id=None) -> Response:
        if id is None:
            notifications = [i.to_dict() for i in Notification.query.all()]
            return send_json_response(
                Response200(data={"notifications": notifications})
            )

        notification: Notification = Notification.query.filter_by(id=id).first()
        if notification is None:
            return send_json_response(Response404("Notification Not Found"))

        return send_json_response(
            Response200(data={"notification": notification.to_dict()})
        )

    def post(self) -> Response:
        data = request.json

        try:
            # Attempt to create a new notification && Validate the notification
            notification: Notification = Notification(
                message=data.get("message", None),
                start_date=data.get("start_date", None),
                end_date=data.get("end_date", None),
                channel=data.get("channel", None),
                notification_type=data.get("notification_type", None),
            )

            # Check if the channel is valid for website
            if notification.channel == "WEBITE":
                if data.get("start_date") is None or data.get("end_date") is None:
                    return send_json_response(
                        Response400(
                            "Invalid Request: 'start_date' and 'end_date' are required for WEBSITE notifications"
                        )
                    )

            # Add the notification to the database
            db.session.add(notification)
            db.session.commit()

            # Handle the notification
            if notification.channel == "SMS":
                MessageService().send_sms(notification.message)
            elif notification.channel == "EMAIL":
                MessageService().send_email(notification.message)

            return send_json_response(
                Response200(data={"notification": notification.to_dict()})
            )

        except TwilioRestException as e:
            return send_json_response(Response500(str(e)))

        except ValueError as e:
            return send_json_response(Response400(str(e)))

        except Exception as e:
            return send_json_response(Response500(str(e)))

    def put(self, id) -> Response:
        data = request.json

        # Check if notification exists
        notification: Notification = Notification.query.filter_by(id=id).first()
        if notification is None:
            return send_json_response(Response404("Notification Not Found"))

        # Check if the notification is of channel website
        if notification.channel != "website":
            return send_json_response(
                Response400("Can Only Update Website Notifications")
            )

        try:
            # Update notification
            notification.message = data.get("message", notification.message)
            notification.start_date = data.get("start_date", notification.start_date)
            notification.end_date = data.get("end_date", notification.end_date)
            notification.notification_type = data.get(
                "notification_type", notification.notification_type
            )

            db.session.commit()
            return send_json_response(
                Response200(data={"notification": notification.to_dict()})
            )

        except ValueError as e:
            return send_json_response(Response400(str(e)))

        except Exception as e:
            return send_json_response(Response500(str(e)))

    def delete(self, id) -> Response:
        # Check if notification exists
        notification: Notification = Notification.query.filter_by(id=id).first()
        if notification is None:
            return send_json_response(Response404("Notification Not Found"))

        # Delete notification
        db.session.delete(notification)
        db.session.commit()
        return send_json_response(Response200(f"{id} Deleted"))


# -----------------------------------------------------------------------------
def setup_routes_for_notification(api: Api) -> None:
    api.add_resource(
        NotificationRestClass,
        "/notifications/",
        "/notifications/<uuid:id>",
    )
