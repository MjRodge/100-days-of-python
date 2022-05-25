from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)

class BookForm(FlaskForm):
    title = StringField(
        label="Book Title", 
        validators=[
            InputRequired(), 
            Length(min=3, max=100)
            ]
        )
    author = StringField(
        label="Author", 
        validators=[
            InputRequired(), 
            Length(min=3, max=100)
            ]
        )
    rating = IntegerField(
        label="Rating",
        validators=[
            InputRequired()
        ]
    )

all_books = []


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)

