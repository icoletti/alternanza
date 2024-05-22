from flask import Flask, render_template
import os

HOST = os.environ["HOST"]
PORT = os.environ.get("PORT", 8703)
NAME = os.environ.get("NAME", None)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

@app.route('/hello/')
def hello(name=NAME):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    """ run app """
    app.run(host=HOST, port=PORT)