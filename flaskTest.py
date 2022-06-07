from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class getLatestPrice(Resource):
    pass

class getLatestBar(Resource):
    pass

api.add_resource(getLatestPrice, "/getLatestPrice")

api.add_resource(getLatestBar, "/getLatestPrice")

if __name__ == "__main__":
    app.run()