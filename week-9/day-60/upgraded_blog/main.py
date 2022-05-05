from flask import Flask, render_template, request
import requests
import smtplib
from secrets import my_email, my_password

app = Flask("__main__")

blog_posts = requests.get("https://api.npoint.io/bf0deee3eaa99ae6599c").json()

@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", msg_sent=False)
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            # my_email my_password configured in secrets.py
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="michael@1mrkt.to", msg=f"Subject:blog contact\n\nmsg_from: {name}, email: {email}, phone: {phone}, message: {message}")
        return render_template("contact.html", msg_sent=True)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for blog_post in blog_posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)