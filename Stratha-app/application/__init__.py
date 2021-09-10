from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

#Link database
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('DB_SECRET')

#Ignore track modifications warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Create database object
db = SQLAlchemy(app)

from application import routes