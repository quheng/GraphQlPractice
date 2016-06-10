# coding=utf8
# Author: quheng

from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "works"
