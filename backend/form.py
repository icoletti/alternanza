from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email


def my_length_check(form, field):
    '''controllo della lubghezza user'''
    if len(field.data) > 4:
        raise ValidationError('Field must be less than 4 characters')

def postal_check(form, field):
    '''controllo della lungezza del codice postale, deve essere di 6 cifre'''
    try:
        number = int(field.data)
        if number > 999999:
            raise ValidationError('Field must be less than 999999')
    except ValueError:
        raise ValidationError('It must be a 6-digit number')
    
def validate_digits(form, field):
    '''controllo se ci sono solo cifre nel codice postale'''
    if not field.data.isdigit():
        raise ValidationError('It must be only composed by numbers')

class MyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), my_length_check])
    about = TextAreaField('About', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    region = StringField('Region', validators=[DataRequired()])
    postal_code = StringField('Postal code', validators=[DataRequired(), postal_check, validate_digits])
    submit = SubmitField('Submit')



