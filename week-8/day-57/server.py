from unicodedata import name
from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(0, 10)
    date = datetime.datetime.now()
    current_year = date.strftime("%Y")
    return render_template("index.html", rand_num=random_number, year=current_year)

@app.route("/guess/<name_input>")
def guess(name_input):
    gender_url = f"https://api.genderize.io?name={name_input}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    api_gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name_input}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    api_age = age_data["age"]
    return render_template("name.html", name=name_input, gender=api_gender, age=api_age)

if __name__ == "__main__":
    app.run(debug=True)