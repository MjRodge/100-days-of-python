from unicodedata import name
from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(0, 10)
    date = datetime.datetime.now()
    current_year = date.strftime("%Y")
    return render_template("index.html", rand_num= random_number, year=current_year)

@app.route("/guess/<name_input>")
def guess(name_input):
    return render_template("name.html", name=name_input)

if __name__ == "__main__":
    app.run(debug=True)