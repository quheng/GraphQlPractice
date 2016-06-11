# coding=utf8
# Author: quheng

from flask import Flask
from flask_graphql import GraphQLView


from schema import schema
from database import session


app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

@app.route('/')
@app.route('/index')
def index():
    return "works"
