from flask_wtf import FlaskForm
from wtforms import RadioField, ValidationError, IntegerField
from wtforms.validators import DataRequired, NumberRange


class MyForm(FlaskForm):
    operation = RadioField('Operazione', choices=[('opt1', 'Standard/tanum'), ('best_option', 'Ricorrente')], validators=[DataRequired()])
    payment = RadioField('Pagamento', choices=[('cash', 'Contanti'), ('credit_card', 'Carte'), ('best_option', 'Bonifico')], validators=[DataRequired()])
    billing_info = RadioField('Dati di Fatturazione', choices=[('manual', 'Manuale'), ('best_option', 'Spid')], validators=[DataRequired()])
    quantity = IntegerField('Quantità', validators=[DataRequired(), NumberRange(min=100, max=100000, message='Quantità deve essere tra 100 e 100000')])


def calculate_commission(quantity, operation, payment, billing_info):
    base_commission_rate = 0.10
    if 300 <= quantity < 1000:
        base_commission_rate -= 0.01
    elif 1000 <= quantity < 3000:
        base_commission_rate -= 0.02
    elif 3000 <= quantity < 10000:
        base_commission_rate -= 0.03
    elif 10000 <= quantity < 30000:
        base_commission_rate -= 0.04
    elif quantity >= 30000:
        base_commission_rate -= 0.05


    if operation == 'best_option':
        base_commission_rate -= 0.01
    if payment == 'best_option':
        base_commission_rate -= 0.01
    if billing_info == 'best_option':
        base_commission_rate -= 0.01

    commission = round(quantity * base_commission_rate, 2)
    
    return commission