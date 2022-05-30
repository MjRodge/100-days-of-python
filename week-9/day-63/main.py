from crypt import methods
from flask import Flask, redirect, render_template, url_for, request
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



@app.route('/')
def home():
    all_books = db.session.query(BookData).all()
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

@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = BookData.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = BookData.query.get(book_id)
    return render_template("edit.html", book=book_selected)

@app.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_delete = BookData.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    all_books = db.session.query(BookData).all()
    return render_template("index.html", books=all_books)


if __name__ == "__main__":
    app.run(debug=True)

