from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email

app = Flask(__name__)
app.secret_key = "a-secret-key-for-flask-that-id-usually-store-in-a-secret-store-or-env-file"

class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        [
            Email(message=("not a valid email address")),
            InputRequired()
        ]
    )
    password = PasswordField(
        "Password",
        [
            Length(
                min=8,
                message=("password should be at least 8 characters")
            ),
            InputRequired()
        ]
    )
    submit = SubmitField("submit")



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)