from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///multiverse.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

from .routes import *
