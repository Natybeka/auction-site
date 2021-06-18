from flask import Flask, request
from flask.blueprints import Blueprint
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_restplus import Api, Resource, fields
from werkzeug import cached_property

from schema import *

items = Blueprint("items", __name__, url_prefix="/items")
CORS(items, supports_credentials=True)
api = Api(items, version='1.0', title='DagmEbay API', 
          description="API for the dagm Ebay web serivce")

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

item = api.model("Item", {
    'ItemId':fields.String,
    'ItemName': fields.String,
    'Category':fields.String,
    'Description': fields.String, 
    'Image': fields.String,
    'SellerId': fields.String
}) 


@api.route('/item/<string:itemname>')
class userResource(Resource):
    def get(self, itemname):
        # to display one item
        user = Item.query.filter_by(ItemId=itemname).first()
        return item_schema.dump(user)
    
    # to update an item
    @api.expect(item)
    @api.response(204, 'Item updated')
    def put(self, itemname):
        item = Item.query.filter_by(ItemName=itemname).first()
        # item.ItemId = "1"
        item.ItemName = request.json['ItemName']
        item.Category = request.json['Category']
        item.Description = request.json['Description']
        item.Image = request.json['Image']
        item.SellerId = request.json['SellerId']
        
        db.session.add(item)
        db.session.commit()
        
        return item_schema.dump(item)
    
    #to remove an item
    @api.response(204, 'Item successfully deleted.')
    def delete(self, itemname):
        """
        Deletes Item.
        """
        item = Item.query.filter_by(ItemName=itemname).first()
        if item is None:
            return None, 404
        db.session.delete(item)
        db.session.commit()
        return None, 204
        
@api.route('/items')
class userResource(Resource):
    # get all the itmes
    def get(self):
        """
        Get all the items
        """
        items = Item.query.all()
        return items_schema.dump(items)
    
    @api.expect(item)
    def post(self):
        # creates a new user
        
        new_item = Item()
        new_item.ItemId = request.json['ItemId']
        new_item.ItemName = request.json['ItemName']
        new_item.Category = request.json['Category']
        new_item.Description = request.json['Description']
        new_item.Image = request.json['Image']
        new_item.SellerId = request.json['SellerId']
        
        db.session.add(new_item)
        db.session.commit()
        
        return item_schema.dump(new_item)