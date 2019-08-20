# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:40:01 2019

@author: Itachi
"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return  {'Test': 'ddfsgsfgfgdhfgfh'}
    
    def post(self):
        some_json = request.get_json()
        return {'you sent :': some_json}
    
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)