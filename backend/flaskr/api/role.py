from flask import Response, request
from flask_restful import Resource, Api
from ..models.models import db, UserRole
from .response import Response200, Response400, Response404, send_json_response

class UserRoleRestClass(Resource):
    def get(self, role_id=None) -> Response:
        if role_id is None:
            roles_dict = [role.to_dict() for role in UserRole.query.all()]
            return send_json_response(Response200(data={"roles": roles_dict}))

        role: UserRole = UserRole.query.filter_by(id=role_id).first()
        if role is None:
            return send_json_response(Response404("Role Not Found"))

        return send_json_response(Response200(data={"role": role.to_dict()}))

    def post(self) -> Response:
        data = request.json

        # Check if role exists already
        role: UserRole = UserRole.query.filter_by(role_name=data["role_name"]).first()
        if role is not None:
            return send_json_response(Response400("Role Already Exists"))

        # Create role
        role: UserRole = UserRole(
            role_name=data.get("role_name"), permissions=data.get("permissions")
        )
        db.session.add(role)
        db.session.commit()
        return send_json_response(Response200(data={"role": role.to_dict()}))

    def put(self, role_id) -> Response:
        data = request.json

        # Check if role exists
        role: UserRole = UserRole.query.filter_by(id=role_id).first()
        if role is None:
            return send_json_response(Response404("Role Not Found"))

        # Check if new name is already taken
        if data.get("role_name", None) is not None:
            role: UserRole = UserRole.query.filter_by(
                role_name=data.get("role_name")
            ).first()
            if role is not None:
                return send_json_response(
                    Response400(f"Role Name '{data.get('role_name')}' Already Exists")
                )

        # Update role
        role.role_name = data.get("role", role.role_name)
        role.permissions = data.get("permissions", role.permissions)
        db.session.commit()
        return send_json_response(Response200(data={"role": role.to_dict()}))

    def delete(self, role_id) -> Response:
        # Check if role exists
        role: UserRole = UserRole.query.filter_by(id=role_id).first()
        if role is None:
            return send_json_response(Response404("Role Not Found"))

        # Delete role
        db.session.delete(role)
        db.session.commit()
        return send_json_response(Response200(f"{role_id} Deleted"))


def setup_routes_for_user_role(api: Api) -> None:
    api.add_resource(UserRoleRestClass, "/roles/", "/roles/<uuid:role_id>")
