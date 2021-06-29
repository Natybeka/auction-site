from flask import Flask, request, jsonify
from flask.blueprints import Blueprint
from flask_marshmallow import Marshmallow
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
import json
import attr
from werkzeug import cached_property

from schema import *

auctions = Blueprint("auction", __name__, url_prefix="/auction")

CORS(auctions, supports_credentials=True)
api = Api(auctions, version='1.0', title='DagmEbay API',
          description="API for the dagm Ebay web serivce")

auction_schema = AuctionSchema()
auctions_schema = AuctionSchema(many=True)

auction = api.model("Auction", {
    'AuctionId': fields.String,
    'ItemId': fields.String,
    'StartDate': fields.DateTime,
    'EndDate': fields.DateTime,
    'InitialPrice': fields.Float,
    'CurrentPrice': fields.Float,
    'IsCompleted': fields.Boolean,
    'HigestBidder': fields.String,

})


@api.route('/auction/<string:auctionId>')
class userResource(Resource):
    def get(self, auctionId):
        # to display one user
        auction = Auction.query.filter_by(AuctionId=auctionId).first()
        auctionDict = {}
        auctionDict['id'] = auction.AuctionId
        auctionDict['startDate'] = auction.StartDate
        auctionDict['endDate'] = auction.EndDate
        auctionDict['currentHighest'] = auction.CurrentPrice
        auctionDict['startingPrice'] = auction.InitialPrice
        auctionDict['highestBidder'] = auction.HighestBidder
        auctionDict['item'] = {}
        item = Item.query.filter_by(ItemId=str(auction.ItemId)).first()
        auctionDict['item']['id'] = item.ItemId
        auctionDict['item']['name'] = item.ItemName
        auctionDict['item']['description'] = item.Description
        auctionDict['item']['owner_id'] = item.SellerId
        auctionDict['item']['category'] = item.Category
        auctionDict['item']['image'] = item.Image
        auctionDict['bids'] = []
        allBids = Bid.query.filter_by(
            AuctionId=auction.AuctionId).all()
        for bid in allBids:
            auctionDict['bids'].append({
                "id": bid.BidId,
                "amount": bid.Amount,
                "bid_date": bid.Date,
                "bidder_id": bid.UserId
            })
            auctionDict['bids'].reverse()
        return jsonify(auctionDict)

     # to update an auction

    @api.expect(auction)
    @api.response(204, 'Auction updated')
    def put(self, auctionId):
        auction = Auction.query.filter_by(AuctionId=auctionId).first()
        # item.ItemId = "1"
        auction.CurrentPrice = request.json['latestBid']
        auction.HighestBidder = request.json['latestBidder']

        db.session.add(auction)
        db.session.commit()

        return auction_schema.dump(auction)

    # to remove an auction
    @api.response(204, 'Auction successfully deleted.')
    def delete(self, auctionId):
        """
        Deletes Dinner.
        """
        auction = Auction.query.filter_by(AuctionId=auctionId).first()
        if auction is None:
            return None, 404
        db.session.delete(auction)
        db.session.commit()
        return None, 204


@api.route('/auction')
class userResource(Resource):
    def get(self):
        """
        Get all the auctions
        """

        auctions = Auction.query.all()
        returnArr = []
        profile = {}
        for auction in auctions:
            auctionDict = {}
            auctionDict['id'] = auction.AuctionId
            auctionDict['startDate'] = auction.StartDate
            auctionDict['endDate'] = auction.EndDate
            auctionDict['startingPrice'] = auction.InitialPrice
            auctionDict['currentHighest'] = auction.CurrentPrice
            auctionDict['highestBidder'] = auction.HighestBidder
            # Item part
            auctionDict['item'] = {}
            item = Item.query.filter_by(ItemId=str(auction.ItemId)).first()
            auctionDict['item']['id'] = item.ItemId
            auctionDict['item']['name'] = item.ItemName
            auctionDict['item']['description'] = item.Description
            auctionDict['item']['owner_id'] = item.SellerId
            auctionDict['item']['category'] = item.Category
            auctionDict['item']['image'] = item.Image

            # Bid part
            auctionDict['bids'] = []
            allBids = Bid.query.filter_by(
                AuctionId=auction.AuctionId).all()
            for bid in allBids:
                auctionDict['bids'].append({
                    "id": bid.BidId,
                    "amount": bid.Amount,
                    "bid_date": bid.Date,
                    "bidder_id": bid.UserId
                })
            returnArr.append(auctionDict)
        
        # return auctions_schema.dump(auction)
        return jsonify(returnArr)

    @api.expect(auction)
    def post(self):
        # creates a new user

        new_auction = Auction()
        new_auction.AuctionId = request.json['AuctionId']
        new_auction.ItemId = request.json['ItemId']
        new_auction.StartDate = request.json['StartDate']
        new_auction.EndDate = request.json['EndDate']
        new_auction.InitialPrice = request.json['InitialPrice']
        new_auction.CurrentPrice = request.json['CurrentPrice']
        new_auction.IsCompleted = request.json['IsCompleted']
        new_auction.HighestBidder = request.json['HighestBidder']

        db.session.add(new_auction)
        db.session.commit()

        return auction_schema.dump(new_auction)
