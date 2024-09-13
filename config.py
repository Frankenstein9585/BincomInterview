import logging

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


import routes