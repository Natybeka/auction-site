from flask import Flask, request
from flask.blueprints import Blueprint
from flask_marshmallow import Marshmallow
from flask_restplus import Api, Resource, fields
from werkzeug import cached_property
from flask_cors import CORS, cross_origin

from schema import *

auth = Blueprint("auth", __name__, url_prefix="/auth")
# Set up schema to access the info from the database

CORS(auth, supports_credentials=True)

api = Api(auth, version='1.0', title='DagmEbay API',
          description="API for the dagm Ebay web serivce")

# first one to access 1, second one to access many
user_schema = UserSchema()
users_schema = UserSchema(many=True)

ma = Marshmallow(auth)

# Model required by flask_restplus for expect

user = api.model("User", {
    'UserId': fields.String,
    'Username': fields.String,
    'Password': fields.String,
    'FirstName': fields.String,
    'LastName': fields.String,
    'Email': fields.String,
    'Address': fields.String,
    'PhoneNumber': fields.String,
    'Rating': fields.Integer
})


@api.response(200, 'Return found users')
@api.route('/users/<string:userId>')
class userResource(Resource):
    def get(self, userId):
        # to display one user

        user = User.query.filter_by(UserId=userId).first()
        return user_schema.dump(user)
    def put(self, userId):
        user = User.query.filter_by(UserId=userId).first()
        user.FirstName = request.json['FirstName']
        user.LastName = request.json['LastName']
        user.PhoneNumber = request.json['PhoneNumber']
        user.Address = request.json['Address']
        db.session.add(user)
        db.session.commit()

@api.response(200, "Return found username")
@api.route('/checkusername/<string:username>')
class userResource(Resource):
    def get(self, username):
        user = User.query.filter_by(Username=username).first()
        if user:
            return 200
        else:
            return 409


# Route to Check User Firebase ID


@api.route("/getuser/<firebase_id>")
class userResource(Resource):
    def get(self, firebase_id):
        user = User.query.filter_by(UserId=firebase_id).first()
        if(user):
            response_object = {
                "code": "Error",
                "message": "firebase_id already in database"
            }
            return(response_object)
        response_object = {"code": "Success"}
        return (response_object)


@api.route("/signuser")
class Register(Resource):
    def post(self):
        # try:
        response_object = {'status': 'success'}
        post_data = request.get_json()['user_info']
        userId = post_data['UserId']
        username = post_data['Username']
        firstName = post_data['FirstName']
        lastName = post_data['LastName']
        email = post_data['Email']
        address = post_data['Address']
        phoneNumber = post_data['PhoneNumber']
        rating = post_data['Rating']

        print("here")

        new_user = User(UserId=userId, Username=username, FirstName=firstName, LastName=lastName,
                        Email=email, Address=address, PhoneNumber=phoneNumber, Rating=rating)
        db.session.add(new_user)
        db.session.commit()
        print('here again')
        return (response_object), 200
        # except:
        # print("Here")


@api.route('/users')
class userResource(Resource):

    @api.expect(user)
    def post(self):
        # creates a new user

        new_user = User()
        new_user.UserId = request.json['UserId']
        new_user.Username = request.json['Username']
        new_user.Password = request.json['Password']
        new_user.FirstName = request.json['FirstName']
        new_user.LastName = request.json['LastName']
        new_user.Email = request.json['Email']
        new_user.Address = request.json['Address']
        new_user.PhoneNumber = request.json['PhoneNumber']
        new_user.Rating = 0

        check = User.query.filter_by(Username=new_user.Username).first()
        if check is not None:
            return 409

        db.session.add(new_user)
        db.session.commit()

        return user_schema.dump(new_user)
