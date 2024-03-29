from crypt import methods
from datetime import date
from operator import index
from time import strftime
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = StringField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


## Routes

# GET index
@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


# GET single post by id
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = db.session.query(BlogPost).get(index)
    return render_template("post.html", post=requested_post)


# GET form for creating a new post
# POST write form contents to db
@app.route("/make-post", methods=["GET", "POST"])
def make_post():
    post_form = CreatePostForm()
    if request.method == "POST":
        if post_form.validate_on_submit():
            today = date.today()
            new_post = BlogPost(
                title = request.form.get("title"),
                subtitle = request.form.get("subtitle"),
                author = request.form.get("author"),
                img_url = request.form.get("img_url"),
                body = request.form.get("body"),
                date = today.strftime("%B %d, %Y")
            ) 
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=post_form)


# GET form to edit selected post
# POST send updates to row in db
@app.route("/edit-post", methods=["GET", "POST"])
def edit_post():
    post_to_edit = request.args.get("post_id")
    requested_post = db.session.query(BlogPost).get(post_to_edit)
    edit_form = CreatePostForm(
        title=requested_post.title,
        subtitle=requested_post.subtitle,
        img_url=requested_post.img_url,
        author=requested_post.author,
        body=requested_post.body
    )
    return render_template("make-post.html", form=edit_form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)