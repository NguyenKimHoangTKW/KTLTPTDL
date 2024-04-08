from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = '!@#@!#ASDASFAER!@$ASD#!#@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hoang@localhost/dbthptqg2023'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 15

db = SQLAlchemy(app=app)