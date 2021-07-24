from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api, Namespace, fields

app = Flask(__name__)

app.config.from_pyfile("main.cfg")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



