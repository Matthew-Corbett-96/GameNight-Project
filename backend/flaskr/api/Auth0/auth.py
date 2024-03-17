from flask import Response
from flask_restful import Resource, Api
from ...models.models import User
from ..response import Response200, Response404, send_json_response

class UserAuth0Class(Resource):
        def get(self, auth0_id: str) -> Response:
            user: User = User.query.filter_by(auth0_id=auth0_id).first()
            if user is None:
                return send_json_response(Response404('User Not Found'))
            # TODO: Send a 201 instead of a 200
            return send_json_response(Response200(data={"user" : user.to_dict()}))



def setup_routes_for_auth0(api: Api) -> None:
    api.add_resource(UserAuth0Class,
                    "/auth0/users/<string:auth0_id>"
                    )
