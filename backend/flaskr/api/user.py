from flask_restful import Resource, Api
from flask import Response, request, jsonify, make_response
from .response import Response200, Response400, Response404, Response201, send_json_response
from ..models.models import db, User, UserRole


class UserRestClass(Resource):
    def get(self, user_id=None) -> Response:
        if user_id is None:
            users_dict: list[dict] = [user.to_dict() for user in User.query.all()]
            response: dict = Response200(data={"Users": users_dict}).to_dict()
            return make_response(jsonify(response), 200)

        user: User = User.query.filter_by(id=user_id).first()
        if user is None:
            return make_response(jsonify(Response404("User Not Found").to_dict()), 404)

        response = Response200(data={"User": user.to_dict()}).to_dict()
        return make_response(jsonify(response), 200)

    def post(self) -> Response:
        data = request.json

        # Check if email exists already
        if User.query.filter_by(email=data["email"]).first() is not None:
            return send_json_response(
                Response400(message=f"Email '{data.get('email')}' Already Exists")
            )

        # Check if username exists already
        if User.query.filter_by(username=data["username"]).first() is not None:
            return send_json_response(
                Response400(message=f"Username '{data.get('username')}' Already Exists")
            )

        # Check if auth0_id exists already
        if User.query.filter_by(auth0_id=data["auth0_id"]).first() is not None:
            return send_json_response(
                Response400(message=f"Auth0 Id '{data.get('auth0_id')}' Already Exists")
            )

        # Check if role exists so we can assign to user
        role = None
        if data.get("role", None) is not None:
            role: UserRole = UserRole.query.filter_by(role_name=data["role"]).first()
            if role is None:
                return send_json_response(
                    Response400(message=f"Role'{data.get('role')}' Not Found")
                )

        phone = None
        if data.get("phone_number", None) is not None:
            phone: str = data["phone_number"]
            if User.query.filter_by(phone_number=phone).first() is not None:
                return send_json_response(
                    Response400(
                        message=f"Phone Number '{data.get('phone_number')}' Already Exists"
                    )
                )

        user: User = User(
            auth0_id=data.get("auth0_id"),
            username=data.get("username"),
            first_name=data.get("first_name", None),
            last_name=data.get("last_name", None),
            gender=data.get("gender", None),
            email=data.get("email"),
            phone_number=phone if phone is not None else None,
            role_id=role.id if role is not None else None,
            is_active=data.get("is_active", True),
        )
        db.session.add(user)
        db.session.commit()

        return send_json_response(Response201(data={"User": user.to_dict()}))

    def put(self, user_id) -> Response:
        data = request.json

        # Check if user exists
        user: User = User.query.filter_by(id=user_id).first()
        if user is None:
            return send_json_response(Response404("User Not Found"))

        # if username --> Check if username is already taken
        if data.get("username", None) is not None:
            if data["username"] != user.username:
                if User.query.filter_by(username=data["username"]).first() is not None:
                    return send_json_response(
                        Response400(
                            message=f"Username '{data.get('username')}' Already Exists"
                        )
                    )

        # if email --> Check if email is already taken
        if data.get("email", None) is not None:
            if data["email"] != user.email:
                if User.query.filter_by(email=data["email"]).first() is not None:
                    return send_json_response(
                        Response400(
                            message=f"Email '{data.get('email')}' Already Exists"
                        )
                    )

        # if auth0_id --> Check if auth0_id is already taken
        if data.get("auth0_id", None) is not None:
            if data["auth0_id"] != user.auth0_id:
                if User.query.filter_by(auth0_id=data["auth0_id"]).first() is not None:
                    return send_json_response(
                        Response400(
                            message=f"Auth0 Id '{data.get('auth0_id')}' Already Exists"
                        )
                    )

        # if role --> Check if role exists so we can assign to user
        role = None
        if data.get("role", None) is not None:
            role: UserRole = UserRole.query.filter_by(role_name=data["role"]).first()
            if role is None:
                return send_json_response(
                    Response400(message=f"Role'{data.get('role')}' Not Found")
                )

        # if phone_number --> Check if phone_number is already taken
        if data.get("phone_number", None) is not None:
            if (
                User.query.filter_by(phone_number=data["phone_number"]).first()
                is not None
            ):
                return send_json_response(
                    Response400(
                        message=f"Phone Number '{data.get('phone_number')}' Already Exists"
                    )
                )

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
            return send_json_response(Response404("User Not Found"))

        db.session.delete(user)
        db.session.commit()
        return send_json_response(Response200(f"{user_id} Deleted"))


def setup_routes_for_user(api: Api) -> None:
    api.add_resource(UserRestClass, "/users/", "/users/<uuid:user_id>")
