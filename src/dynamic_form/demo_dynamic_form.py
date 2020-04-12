from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, IntegerField

class demo_dynamic_form(FlaskForm):
    First_Name = StringField('First Name', validators=[DataRequired()])
    Last_Name = StringField('Last Name', validators=[DataRequired()])
    Email = EmailField('Email', validators=[DataRequired()])
    Address = StringField('Address', validators=[DataRequired()])
    City = StringField('City', validators=[DataRequired()])
    Province = StringField('Province', validators=[DataRequired()])
    Postal_Code = IntegerField('Postal Code', validators=[DataRequired()])
    Country = StringField('Country', validators=[DataRequired()])
    Job_Title = StringField('Job Title', validators=[DataRequired()])
    Contract_Duration = StringField('Contract Duration', validators=[DataRequired()])
    Next = SubmitField('Next', validators=[DataRequired()])
    