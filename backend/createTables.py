from flask import Flask,request

from dbModels import *

app = Flask(__name__)

app.config['SERVER_NAME'] = "localhost:8888"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/dagmebaydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def main():
    db.create_all()


if __name__ =='__main__':
    with app.app_context():
        main()
