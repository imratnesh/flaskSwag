from flask import Flask 
from flask_restplus import Api, Resource

flask_app =Flask(__name__)

app = Api(app=flask_app)

name_space = app.namespace('ratnesh', description='Ratnesh APIs')


@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
				"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}


if __name__ == '__main__':
    flask_app.run(debug=True)