from application import db
from datetime import datetime



class User(db.Model):
    __tablename__ = "users"
    UserId = db.Column(db.String, primary_key=True)
    Username = db.Column(db.String, unique=True)
    
    FirstName = db.Column(db.String, nullable=False)
    LastName = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, nullable=False)
    Address = db.Column(db.String, nullable=False)
    PhoneNumber = db.Column(db.String, nullable=False)
    Rating = db.Column(db.Integer, nullable=True)

    
class Item(db.Model):
    __tablename__ = "items"
    ItemId = db.Column(db.String, primary_key=True)
    ItemName = db.Column(db.String, nullable=False)
    Category = db.Column(db.String, nullable=False)
    Description = db.Column(db.Text, nullable=False)
    Image = db.Column(db.String, nullable=False)
    SellerId = db.Column(db.String, db.ForeignKey(
        "users.UserId"), nullable=False)

class Bid(db.Model):
    __tablename__ = "bids"
    AuctionId = db.Column(db.Integer, db.ForeignKey(
        "auctions.AuctionId"), nullable=False)
    BidId = db.Column(db.String, primary_key=True)
    UserId = db.Column(db.String, db.ForeignKey(
        "users.UserId"), nullable=False)
    Amount = db.Column(db.Float, nullable=False)
    Date = db.Column(db.DateTime, nullable=False)
    
class Auction(db.Model):
    __tablename__ = "auctions"
    AuctionId = db.Column(db.Integer, primary_key=True)
    ItemId = db.Column(db.String, db.ForeignKey(
        "items.ItemId"), nullable=False)
    StartDate = db.Column(db.DateTime, nullable=False)
    EndDate = db.Column(db.DateTime, nullable=False)
    InitialPrice = db.Column(db.Float, nullable=False)
    CurrentPrice = db.Column(db.Float, nullable=False)
    IsCompleted = db.Column(db.Boolean, nullable=False)
    HighestBidder = db.Column(db.String, db.ForeignKey(
        "users.UserId"),nullable=False)
    
class Review(db.Model):
    __tablename__ = "reviews"
    ReviewId = db.Column(db.String, primary_key=True)
    SellerId = db.Column(db.String, db.ForeignKey(
        "users.UserId"), nullable=False)
    ReviewerId = db.Column(db.String, db.ForeignKey(
        "users.UserId"), nullable=False)
    Description = db.Column(db.Text, nullable=False)
    Date = db.Column(db.DateTime, nullable=False)
    Rating = db.Column(db.Integer, nullable=False)
    
    

    