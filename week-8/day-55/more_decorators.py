from flask import Flask

app = Flask(__name__)


def make_bold(text):
    def emph_wrap():
        return "<em>"+text()+"</em"
    return emph_wrap()


@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello, World!</p>"
