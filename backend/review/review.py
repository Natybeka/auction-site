from flask import Flask, request
from flask.blueprints import Blueprint
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_restplus import Api, Resource, fields
from werkzeug import cached_property

from schema import *

reviews = Blueprint("reviews", __name__, url_prefix="/reviews")
CORS(reviews, supports_credentials=True)
api = Api(reviews, version='1.0', title='DagmEbay API', 
          description="API for the dagm Ebay web serivce")

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

review = api.model("review", {
    'ReviewId':fields.String,
    'SellerId': fields.String,
    'ReviewerId':fields.String,
    'Description': fields.String, 
    'Date': fields.DateTime,
    'Rating': fields.Integer
}) 


@api.route('/review/<string:reviewId>')
class userResource(Resource):
    def get(self, reviewId):
        # to display one review
        user = review.query.filter_by(ReviewId=reviewId).first()
        return review_schema.dump(user)
    
    # to update an review
    @api.expect(review)
    @api.response(204, 'review updated')
    def put(self, reviewId):
        review = Review.query.filter_by(ReviewId=reviewId).first()
        # review.reviewId = "1"
        review.ReviewId = request.json['ReviewId']
        review.SellerId = request.json['SellerId']
        review.ReviewerId = request.json['ReviewerId']
        review.Description = request.json['Descirption']
        review.Date = datetime.now()
        review.Rating = request.json['Rating']
        
        db.session.add(review)
        db.session.commit()
        
        return review_schema.dump(review)
    
    #to remove an review
    @api.response(204, 'review successfully deleted.')
    def delete(self, reviewId):
        """
        Deletes Review.
        """
        review = Review.query.filter_by(reviewId=reviewId).first()
        if review is None:
            return None, 404
        db.session.delete(review)
        db.session.commit()
        return None, 204
        
@api.route('/reviews')
class userResource(Resource):
    # get all the itmes
    def get(self):
        """
        Get all the reviews
        """
        reviews = Review.query.all()
        return reviews_schema.dump(reviews)
    
    @api.expect(review)
    def post(self):
        # creates a new user
        
        new_review = Review()
        new_review.ReviewId = request.json['ReviewId']
        new_review.SellerId = request.json['SellerId']
        new_review.ReviewerId = request.json['ReviewerId']
        new_review.Description = request.json['Description']
        new_review.Date = datetime.now()
        new_review.SellerId = request.json['SellerId']
        
        db.session.add(new_review)
        db.session.commit()
        
        return review_schema.dump(new_review)