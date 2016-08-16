import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oroka:oroka@localhost/orokadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Result


@app.route('/')
def hello():
	return "Hello Flask!"

@app.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)


if __name__ == '__main__':
	app.run()