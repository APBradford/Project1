from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Link database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

app.config['SECRET_KEY'] = 'Test'

#Ignore track modifications warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Create database object
db = SQLAlchemy(app)

from application import routes