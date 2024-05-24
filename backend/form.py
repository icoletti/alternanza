from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FieldList
from wtforms.validators import DataRequired, Email

class MyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about = TextAreaField('About', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    country = FieldList('Country', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    region = StringField('Region', validators=[DataRequired()])
    postal_code = StringField('Postal code', validators=[DataRequired()])
    submit = SubmitField('Submit')


