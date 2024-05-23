from flask import Flask, render_template, request
import os

HOST = os.environ["HOST"]
PORT = os.environ.get("PORT", 8703)

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
      username = request.form.get("username")
      about = request.form.get("about")
      first_name = request.form.get("fname")
      last_name = request.form.get("lname")
      email = request.form.get("email")
      country = request.form.get("country")
      address = request.form.get("street-address")
      city = request.form.get("city")
      region = request.form.get("region")
      postal_code = request.form.get("postal-code")
      data = "I tuoi dati sono: "
      data += "username: "+username+", dettagli: " +about+", nome: "  +first_name+", cognome: "  +last_name+", email: "  +email 
      data += ", paese: " +country +", indirizzo: " +address+", città: " +city+", regione: " +region+", codice postale: " +postal_code
      return data
    return render_template('form.html')


if __name__ == "__main__":
    """ run app """
    app.run(host=HOST, port=PORT)