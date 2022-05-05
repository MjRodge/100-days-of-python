from flask import Flask, render_template
import requests

app = Flask("__main__")

blog_posts = requests.get("https://api.npoint.io/bf0deee3eaa99ae6599c").json()

@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)

@app.route("/contact")
def contact():
    return render_template("contact.html")

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