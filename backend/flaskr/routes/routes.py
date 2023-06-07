from flask import Flask, Response, request, jsonify, make_response
from flask_restful import Resource, Api

def setup_routes(app: Flask, api: Api) -> None:

   fakeDatabase = {
      1: 'Buy groceries',
      2: 'Learn Python',
      3: 'Learn Flask',
      4: 'Build an API'
   }

   # User model
   class TodoSimple(Resource):
      def get(self, todo_id=None):
         if todo_id is None:
            return make_response(jsonify(fakeDatabase), 200)
         return make_response(jsonify({todo_id: fakeDatabase[todo_id]}), 200)

      def put(self, todo_id):
         data = request.json
         fakeDatabase[todo_id] = data['name']
         return {todo_id: fakeDatabase[todo_id]}

   api.add_resource(TodoSimple, '/items/', '/items/<int:todo_id>')


   @app.route('/healthcheck', methods=['GET'])
   def heathcheck() -> Response:
      return make_response(jsonify({'message': 'OK'}), 200)
