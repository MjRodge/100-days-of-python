from pydoc import describe
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=False)
    img_link = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return f'<Movie {self.title}>'
db.create_all()


@app.route('/')
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)


if __name__ == '__main__':
    app.run(debug=True)
