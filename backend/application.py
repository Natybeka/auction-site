from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_restplus import Api, Resource, fields
from werkzeug import cached_property
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)

CORS(app, supports_credentials=True)
# app configuration settings


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

# Set up the database
# db = SQLAlchemy(app)

db = SQLAlchemy(app)

# some imports to avoid circular import
from dbModels import *
from schema import *
from auth.auth import auth
from items.items import items
from auction.auction import auctions
from bids.bids import bids
from review.review import reviews

db.create_all()

# reigster the blueprints
app.register_blueprint(auth)
app.register_blueprint(items)
app.register_blueprint(auctions)
app.register_blueprint(bids)
app.register_blueprint(reviews)

@app.route("/")
def index():
    return "404 Not found"

   