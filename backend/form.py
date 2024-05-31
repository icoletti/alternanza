from flask_wtf import FlaskForm
from wtforms import RadioField, IntegerField, SelectField, FieldList, FormField
from wtforms.validators import DataRequired, NumberRange, InputRequired
import os
import sys
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


# Parametri definiti nel .env
quantity_ranges =  list(map(int, os.environ.get("QUANTITY_RANGES").split(',')))
commission_rates = list(map(float, os.environ.get("COMMISSION_RATES").split(',')))
best_option_adjustment = float(os.environ.get("BEST_OPTION_ADJUSTMENT"))
base_commission = float(os.environ.get("BASE_COMMISSION"))

# Form per le sottocategorie
class SubCategoryForm(FlaskForm):
    option = RadioField('Option', choices=[], validators=[InputRequired()])

class MyForm(FlaskForm):
    operation = RadioField('Operazione', choices=[('opt1', 'Standard/tanum'), ('best_option0', 'Ricorrente')], validators=[DataRequired()])
    # best_option_option = RadioField('Operazioni Ricorrenti', choices=[('sub1', 'Bisettimanale'), ('sub2', 'Mensile'), ('sub3', 'Trimestrale')], validators=[DataRequired()])
    # standard_option = RadioField('Operazioni Standard', choices=[('sub1', '1-2 giorni lavorativi'), ('sub2', '"Fast" (50 euro)')], validators=[DataRequired()])
    payment = RadioField('Pagamento', choices=[('cash', 'Contanti'), ('credit_card', 'Carte'), ('best_option1', 'Bonifico')], validators=[DataRequired()])
    billing_info = RadioField('Dati di Fatturazione', choices=[('manual', 'Manuale'), ('best_option2', 'Spid')], validators=[DataRequired()])
    quantity = IntegerField('Quantità', validators=[DataRequired(), NumberRange(min=100, max=100000, message='Quantità deve essere tra 100 e 100000')])
    subcategories1 = FieldList(FormField(SubCategoryForm), min_entries=3, max_entries=3)
    subcategories2 = FieldList(FormField(SubCategoryForm), min_entries=2, max_entries=2)
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.category_descriptions = {
            'opt1': 'Descrizione breve per Categoria 1',
            'best_option0': 'Descrizione breve per Categoria 2',
            'cash': 'Descrizione breve per Categoria 2',
            'credit_card': 'Descrizione breve per Categoria 2',
            'best_option1': 'Descrizione breve per Categoria 2',
            'manual': 'Descrizione breve per Categoria 2',
            'best_option2': 'Descrizione breve per Categoria 2',
        }



def create_form():
    form = MyForm()
    

def calculate_purchase_btc(quantity, price):
    return (quantity / price)

def calculate_commission(quantity, operation, payment, billing_info, price):
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

