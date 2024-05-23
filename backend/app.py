from flask import Flask, render_template
import os

HOST = os.environ["HOST"]
PORT = os.environ.get("PORT", 8703)
NAME = os.environ.get("NAME", None)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base.html')

@app.route('/base/')
def start(name=NAME):
    return render_template('landing.html', name=name)

@app.route('/form/')
def form():
    return render_template('form.html')


if __name__ == "__main__":
    """ run app """
    app.run(host=HOST, port=PORT)