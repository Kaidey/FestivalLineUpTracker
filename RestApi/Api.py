from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ast
import importlib
import Scrapers

app = Flask(__name__)
api = Api(app)


class Festivals(Resource):

    @app.route("/festivals/<festName>")
    def get(festName):

        assert festName == request.view_args['festName']

        scraper = importlib.import_module('Scrapers.' + festName)

        data = scraper.GetData()
        return {'data': data}, 200


if __name__ == '__main__':
    app.run()
