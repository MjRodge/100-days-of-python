from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    firstname = request.form["firstname"]
    surname = request.form["surname"]
    return f"<h1>firstname: {firstname}, surname: {surname}</h1>"

if __name__ == "__main__":
    app.run(debug=True)