from flask import Flask, render_template, request
import os
import sys
import logging

HOST = os.environ["HOST"]
PORT = os.environ.get("PORT", 8703)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base.html')

@app.route('/info/')
def start():
    return render_template('landing.html')

@app.route('/form/', methods=('GET', 'POST'))
def submit():
    if request.method == "POST":
      logger.info(request.form)
      error = False
      error_message = []
      username = request.form.get("username", None)
      if username != "nomeuser":
          error = True
      about = request.form.get("about")
      if about == "":
        error = True
      first_name = request.form.get("fname")
      if first_name != "nome":
         error = True
      last_name = request.form.get("lname")
      if last_name != "cognome":
         error = True
      email = request.form.get("email")
      if email == "":
         error = True
      country = request.form.get("country")
      if country != "Canada":
         error = True
      address = request.form.get("street-address")
      if address != "indirizzo 1":
         error = True
      city = request.form.get("city")
      if city != "Nessuna":
         error = True
      region = request.form.get("region")
      if region != "Inesistente":
         error = True
      postal_code = request.form.get("postal-code")
      if postal_code != "3422222222":
         error = True
      if error:
         return render_template('result.html', error="sono presenti degli errori")
      else:
         return render_template('result.html',error_message=None, username=username, about=about, first_name=first_name, last_name=last_name, email=email, country=country, address=address, city=city, region=region, postal_code=postal_code)
    return render_template('form.html')


if __name__ == "__main__":
    """ run app """
    app.run(host=HOST, port=PORT)