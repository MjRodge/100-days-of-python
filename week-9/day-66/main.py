from crypt import methods
import json
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

from sqlalchemy import column

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # convert objects to dictionaries for easier, less error-prone, more extensible json api returns
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# render index page at website root
@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record

# GET random cafe
@app.route("/random", methods=["GET"])
def random_cafe():
    # get all cafes with database query
    all_cafes = db.session.query(Cafe).all()
    # generate random cafe item
    random_cafe = random.choice(all_cafes)
    # convert object to dict and return json 
    return jsonify(cafe=random_cafe.to_dict())
    

# GET all cafes
@app.route("/all", methods=["GET"])
def get_all_cafes():
    # get all cafes with database query
    all_cafes = db.session.query(Cafe).all()
    # convert each item into dict and push into json object
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# GET search for cafe by location
@app.route("/search", methods=["GET"])
def search_for_cafe():
    args = request.args
    location_search = args.get("loc")
    print(location_search)
    cafes_in_loc = db.session.query(Cafe).filter_by(location=location_search).all()
    if cafes_in_loc:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes_in_loc])
    else:
        return jsonify(error={"not found": "no cafe found at that location."})


## HTTP POST - Create Record

# POST add new cafe
@app.route("/add", methods=["POST"])
def add_new_cafe():
    form = request.form
    new_cafe = Cafe(
        id = form.get("id"),
        name = form.get("name"),
        map_url = form.get("map_url"),
        img_url = form.get("img_url"),
        location = form.get("loc"),
        seats = form.get("seats"),
        has_toilet = bool(form.get("has_wc")),
        has_wifi = bool(form.get("wifi")),
        has_sockets = bool(form.get("plug")),
        can_take_calls = bool(form.get("calls")),
        coffee_price = form.get("price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    print(new_cafe.name)
    return jsonify(response={"success": "new cafe succesfully submitted"})

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)