from flask import Flask, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "a-secret-key-for-flask-that-id-usually-store-in-a-secret-store-or-env-file"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BookData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f'<Book {self.title}>'
db.create_all()


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
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        # all_books.append({
        #     "author": book_form.author.data,
        #     "title": book_form.title.data,
        #     "rating": book_form.rating.data
        # })
        new_book = BookData(
            title=book_form.title.data, 
            author=book_form.author.data, 
            rating=book_form.rating.data
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=book_form)

if __name__ == "__main__":
    app.run(debug=True)

