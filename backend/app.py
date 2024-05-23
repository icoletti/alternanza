from flask import Flask, render_template, request
import os

HOST = os.environ["HOST"]
PORT = os.environ.get("PORT", 8703)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base.html')

@app.route('/base/')
def start():
    return render_template('landing.html')

@app.route('/form/', methods=('GET', 'POST'))
def form():
    return render_template('form.html')


if __name__ == "__main__":
    """ run app """
    app.run(host=HOST, port=PORT)