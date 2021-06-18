from flask import Flask, request, jsonify
from flask.blueprints import Blueprint
from flask_marshmallow import Marshmallow
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
from werkzeug import cached_property
import uuid

from schema import *

bids = Blueprint("bids", __name__, url_prefix="/bids")
CORS(bids, supports_credentials=True)
api = Api(bids, version='1.0', title='DagmEbay API',
          description="API for the dagm Ebay web serivce")

bid_schema = BidSchema()
bids_schema = BidSchema(many=True)

auction_schema = AuctionSchema()
item_schema = ItemSchema()

bid = api.model("Bid", {
    'BidId': fields.String,
    'AuctionId': fields.String,
    'UserId': fields.String,
    'Amount': fields.Float,
    'Date': fields.DateTime,
})


@api.route('/bid/<string:id>')
class userResource(Resource):
    def get(self, id):
        # to display one bid
        bids = Bid.query.filter_by(UserId=id).all()
        returnArr = []
        for bid in bids:
            auction = Auction.query.filter_by(AuctionId=bid.AuctionId).first()
            item = Item.query.filter_by(ItemId=auction.ItemId).first()
            
            returnArr.append({
                "id" : bid.BidId,
                "amount" : bid.Amount,
                "expiration_date" : auction.EndDate,
                "current_price" : auction.CurrentPrice,
                "item_name" : item.ItemName,
                "item_description" : item.Description,
                "amount": bid.Amount,
                "bid_date": bid.Date,
                "auction_id":bid.AuctionId
            })
        return jsonify(returnArr)

    # to update an bid
    @api.expect(bid)
    @api.response(204, 'bid updated')
    def put(self, bidname):
        bid = Bid.query.filter_by(bidName=bidname).first()
        # bid.bidId = "1"
        

        
        bid.AuctionId = request.json['AuctionId']
        bid.UserId = request.json['UserId']
        bid.Amount = request.json['Amount']
        bid.Date = datetime.now()

        db.session.add(bid)
        db.session.commit()

        return bid_schema.dump(bid)

    # to remove an bid
    @api.response(204, 'bid successfully deleted.')
    def delete(self, bidId):
        """
        Deletes Bid.
        """
        bid = Bid.query.filter_by(BidId=bidId).first()
        if bid is None:
            return None, 404
        db.session.delete(bid)
        db.session.commit()
        return None, 204


@api.route('/bids')
class userResource(Resource):
    # get all the itmes
    def get(self):
        """
        Get all the bids
        """
        bids = Bid.query.all()
        return bids_schema.dump(bids)

    @api.expect(bid)
    def post(self):
        # creates a new user

        uniqueId = str(uuid.uuid4())
        new_bid = Bid()
        new_bid.BidId = uniqueId
        new_bid.AuctionId = request.json['AuctionId']
        new_bid.UserId = request.json['UserId']
        new_bid.Amount = request.json['Amount']
        new_bid.Date = datetime.now()

        db.session.add(new_bid)
        db.session.commit()

        return bid_schema.dump(new_bid)
