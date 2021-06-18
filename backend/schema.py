from flask_marshmallow import Marshmallow
from dbModels import *

schema = Marshmallow()

class UserSchema(schema.Schema):
    class Meta:
        fields = ("UserId", "Username", "FirstName", "LastName",
                  "Email", "Address", "PhoneNumber", "Rating")

        model = User
      
class ItemSchema(schema.Schema):  
    class Meta:
        fields = ("ItemId", "ItemName", "Category", "Description",
                  "Image", "SellerId")

        model = Item
        
class BidSchema(schema.Schema):   
    class Meta:
        fields = ("AuctionId", "BidId", "UserId", "Amount",
                  "Date")

        model = Bid
class AuctionSchema(schema.Schema):   
    class Meta:
        fields = ("AuctionId", "ItemId", "StartDate", "EndDate",
                  "InitialPrice", "HighestPrice", "IsCompleted", "HighestBidder")

        model = Auction
# class TestSchema(schema.Schema):
#     class Meta:
#         fields = ("AuctionId", "ItemId", "StartDate", "EndDate",
#                   "InitialPrice", "HighestPrice", "IsCompleted", "HighestBidder")
#         model = TestModel
class ReviewSchema(schema.Schema):   
    class Meta:
        fields = ("ReviewId", "SellerId", "ReviewerId", "Description",
                  "Date", "Rating")

        model = Review