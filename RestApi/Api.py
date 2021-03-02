from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast
from Scrapers import NosAlive

app = Flask(__name__)
api = Api(app)


class Festivals(Resource):

    def get(self):
        data = NosAlive.GetData()
        return {'data': data}, 200


api.add_resource(Festivals, '/festivals')

if __name__ == '__main__':
    app.run()
