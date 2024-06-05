from flask_wtf import FlaskForm
from wtforms import RadioField, IntegerField
from wtforms.validators import DataRequired, NumberRange
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
    operation = RadioField('Operazione', choices=[('standard', 'Standard/tanum'), ('best_option0', 'Ricorrente')], validators=[DataRequired()])
    operation_sub = RadioField('Operazione Sottoscelta', choices=[('opt1', 'Standard'), ('opt2', '"Fast"'), ('opt3', 'Bisettimanale'), ('opt4', 'Mensile'), ('opt5', 'Trimestrale')], validators=[DataRequired()])
    payment = RadioField('Pagamento', choices=[('cash', 'Contanti'), ('credit_card', 'Carte'), ('best_option1', 'Bonifico')], validators=[DataRequired()])
    billing_info = RadioField('Dati di Fatturazione', choices=[('manual', 'Manuale'), ('best_option2', 'Spid')], validators=[DataRequired()])
    quantity = IntegerField('Quantità', validators=[DataRequired(), NumberRange(min=100, max=100000, message='Quantità deve essere tra 100 e 100000')])
    category_descriptions = {
        'standard': 'Descrizione breve per Standard',
        'best_option0': 'Descrizione breve per Ricorrente', 
        'opt1': '1-2 giorni lavorativi',
        'opt2': 'Costo aggiuntivo di 50 euro',
        'opt3': 'Descrizione breve per Bisettimanale',
        'opt4': 'Descrizione breve per Mensile',
        'opt5': 'Descrizione breve per Trimestrale',
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

def calculate_savings(quantity, operation, payment, billing_info):
    actual_commission = (calculate_commission(quantity, operation, payment, billing_info) / quantity) * 100
    logger.info(actual_commission)
    standard_commission = base_commission
    logger.info(standard_commission)
    savings = standard_commission - actual_commission
    savings_percentage = (savings / standard_commission)*100 if standard_commission > 0 else 0
    return savings_percentage