from flask_wtf import FlaskForm
from wtforms import RadioField, IntegerField, SelectField, FieldList, FormField, StringField
from wtforms.validators import DataRequired, NumberRange, InputRequired
import os
import sys
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


'''Parametri definiti nel .env'''
quantity_ranges =  list(map(int, os.environ.get("QUANTITY_RANGES").split(',')))
commission_rates = list(map(float, os.environ.get("COMMISSION_RATES").split(',')))
best_option_adjustment = float(os.environ.get("BEST_OPTION_ADJUSTMENT"))
base_commission = float(os.environ.get("BASE_COMMISSION"))



class MyForm(FlaskForm):
    '''contenuto del mio form'''
    operation = RadioField('Operazione', choices=[('opt1', 'Standard/tanum'), ('best_option0', 'Ricorrente')], validators=[DataRequired()])
    payment = RadioField('Pagamento', choices=[('cash', 'Contanti'), ('credit_card', 'Carte'), ('best_option1', 'Bonifico')], validators=[DataRequired()])
    billing_info = RadioField('Dati di Fatturazione', choices=[('manual', 'Manuale'), ('best_option2', 'Spid')], validators=[DataRequired()])
    quantity = IntegerField('Quantità', validators=[DataRequired(), NumberRange(min=100, max=100000, message='Quantità deve essere tra 100 e 100000')])
    category_descriptions = {
        'opt1': 'Descrizione breve per Standard',
        'best_option0': 'Descrizione breve per Ricorrente', 
        'cash': 'Descrizione breve per Contanti',
        'credit_card': 'Descrizione breve per Carte', 
        'best_option1': 'Descrizione breve per Bonifico',
        'manual': 'Descrizione breve per Manuale', 
        'best_option2': 'Descrizione breve per Spid',
    }


def calculate_purchase_btc(quantity, price):
    '''metodo per calcolare le commissioni in BTC'''
    return (quantity / price)

def calculate_commission(quantity, operation, payment, billing_info):
    '''metodo per calcolare le commissioni in EURO'''
    for i, range_max in enumerate(quantity_ranges):
        if quantity <= range_max:
            logger.info(quantity)
            logger.info(range_max)
            logger.info(quantity<range_max)
            commission = commission_rates[i]
            if operation == 'best_option0':
                commission += best_option_adjustment
            if payment == 'best_option1':
                commission += best_option_adjustment
            if billing_info == 'best_option2':
                commission += best_option_adjustment
            return (quantity *commission) / 100
    return (commission_rates[-1]) / 100

