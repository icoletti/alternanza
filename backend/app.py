from flask import Flask, render_template, request, flash
import os
import sys
import requests
import logging
from form import MyForm, calculate_commission, calculate_savings
from config import Config
from flask_caching import Cache

KRAKEN_URL = "https://api.kraken.com/0/public/Trades?pair=xbteur"

HOST = os.environ["HOST"]
PORT = os.environ.get("PORT", 8703)

DESCRIZIONE = os.environ.get("DESCRIZIONE_PREZZO", "lol")

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


quantity_ranges =  list(map(int, os.environ.get("QUANTITY_RANGES").split(',')))
logger.info(quantity_ranges)

app = Flask(__name__)
app.config.from_object(Config)

# add cache
cache = Cache(app)

def getprice():
    """getprice from kraken"""

    price_data = cache.get("price")
    if price_data is not None:
        logger.info("passo dalla cache")
        return price_data
    response = requests.get(KRAKEN_URL)
    if response.status_code == 200:
         try:
             data = response.json()
             price = float(data["result"]["XXBTZEUR"][0][0])
             cache.set("price", price)
             logger.info("aggiorno la cache")
             return price
         except KeyError as e:
             return None, f"Errore nella struttura dei dati JSON: {str(e)}"
    else:
        return None, f"Errore nella risposta della chiamata: {response.status_code}"

@app.route("/upload/", methods = ['GET', 'POST'])
def upload():
   form = MyForm()
   price = getprice()
   
   if price is None:
        flash("Errore nel recupero del prezzo corrente. Riprova più tardi.", 'error')
        return render_template('upload.html', form=form, price=None)
   
   if form.validate_on_submit():
      logger.info(request.form)
      invito_boolean = form.invito_boolean.data
      invito_string = form.invito_string.data if invito_boolean == 'best_option' else '-'
      quantity = form.quantity.data
      operation = form.operation.data
      operation_sub = form.operation_sub.data
      payment = form.payment.data
      billing_info = form.billing_info.data
      commission_eur = calculate_commission(quantity, invito_boolean, operation, payment, billing_info)
      actual_price = price + commission_eur
      purchase_btc = quantity / price
      commission_btc = commission_eur / price
      actual_purchase = purchase_btc - commission_btc
      savings_percentange = calculate_savings(quantity, invito_boolean, operation, payment, billing_info)
      smart_options = ['Ricorrente', 'Bonifico', 'Spid']
      boolan_choices = dict(form.invito_boolean.choices)
      operation_choices = dict(form.operation.choices)
      operation_sub_choices = dict(form.operation_sub.choices)
      payment_choices = dict(form.payment.choices)
      billing_info_choices = dict(form.billing_info.choices)
      choices = [
            ('Code invito', boolan_choices.get(invito_boolean, invito_boolean)),
            ('Codice', invito_string),
            ('Operazione', operation_choices.get(operation, operation)),
            ('Sottoscelta operazione', operation_sub_choices.get(operation_sub, operation_sub)),
            ('Pagamento', payment_choices.get(payment, payment)),
            ('Dati di Fatturazione', billing_info_choices.get(billing_info, billing_info)),
        ]

      data = {
      "form": form,
      "quantity": quantity,
      "commission_eur": commission_eur,
      "commission_btc": "%.8f" % commission_btc,
      "commission_percent": round((commission_eur / quantity) * 100, 2),
      "price": price,
      "purchase_btc": "%.8f" % purchase_btc,
      "actual_price": "%.2f" % actual_price,
      "actual_purchase": "%.8f" % actual_purchase,
      "savings_percentange":"%.2f" %  savings_percentange,
      "codice_invito": invito_string,
      "desc": DESCRIZIONE,
      "smart_options": smart_options,
      "choices": choices
      }

      return render_template('result1.html', **data)
   else:
       for field, errors in form.errors.items():
          for error in errors:
             flash(f"Error in the {getattr(form, field).label.text} field - {error}", 'error')
   return render_template('upload.html', form=form, price=price)

@app.route("/")
def home():
    return render_template('base.html')

@app.route('/error/')
def error():
    return render_template('error.html')

if __name__ == "__main__":
    """ run app """
    app.run(host=HOST, port=PORT)