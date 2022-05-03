from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/bf0deee3eaa99ae6599c"
    blog_response = requests.get(blog_url)
    blog_posts = blog_response.json()
    return render_template("index.html", posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)
