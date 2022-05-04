from flask import Flask, render_template
import requests

app = Flask("__main__")

blog_posts = requests.get("https://api.npoint.io/bf0deee3eaa99ae6599c").json()

@app.route("/")
def home():
    print(blog_posts)
    return render_template("index.html", posts=blog_posts)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)