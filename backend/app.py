from flask import Flask, render_template, request, flash
import os
import sys
import requests
import logging
from form import MyForm, calculate_commission

KRAKEN_URL = "https://api.kraken.com/0/public/Trades?pair=xbteur"

HOST = os.environ["HOST"]
PORT = os.environ.get("PORT", 8703)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


quantity_ranges =  list(map(int, os.environ.get("QUANTITY_RANGES").split(',')))
logger.info(quantity_ranges)

app = Flask(__name__)
app.secret_key = 'chiavesegreta1'

def getprice():
    """getprice from kraken"""
    response = requests.get(KRAKEN_URL)
    if response.status_code == 200:
        return response.json()["result"]["XXBTZEUR"][0][0]
    else:
        return render_template('landing.html')

@app.route("/upload/", methods = ['GET', 'POST'])
def upload():
   form = MyForm()
   if form.validate_on_submit():
      logger.info(request.form)
      quantity = form.quantity.data
      operation = form.operation.data
      payment = form.payment.data
      billing_info = form.billing_info.data
      commission = calculate_commission(quantity, operation, payment, billing_info)
      
      data = {
      "form": form,
      "quantity": quantity,
      "commission": commission,
      "commission_percent": round((commission / quantity) * 100, 2),
      }

      return render_template('result1.html', **data)
   else:
       for field, errors in form.errors.items():
          for error in errors:
             flash(f"Error in the {getattr(form, field).label.text} field - {error}", 'error')
   return render_template('upload.html', form=form, price=getprice())

@app.route("/")
def home():
    return render_template('base.html')

@app.route('/info/')
def start():
    return render_template('landing.html')

if __name__ == "__main__":
    """ run app """
    app.run(host=HOST, port=PORT)