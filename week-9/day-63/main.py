from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = "a-secret-key-for-flask-that-id-usually-store-in-a-secret-store-or-env-file"

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
            InputRequired(),
            NumberRange(min=1, max=10)
        ]
    )

all_books = []


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST", "GET"])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        all_books.append({
            "author": book_form.author.data,
            "title": book_form.title.data,
            "rating": book_form.rating.data
        })
        print(all_books)
    return render_template("add.html", form=book_form)

if __name__ == "__main__":
    app.run(debug=True)

