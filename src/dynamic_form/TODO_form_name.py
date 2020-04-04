from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, IntegerField
import pycountry

class GeneralDetails(FlaskForm):
    fname       = StringField('First Name *', validators=[DataRequired()])
    lname       = StringField('Last Name *', validators=[DataRequired()])
    email       = EmailField('Personal Email Address (e.g. xxxxx@gmail.com) *', validators=[DataRequired()])
    address     = StringField('Address *', validators=[DataRequired()])
    city        = StringField('City *', validators=[DataRequired()])
    province    = StringField('Province*', validators=[DataRequired()])
    postal_code = IntegerField('Postal Code*', validators=[DataRequired()])
    country     = SelectField('Country*', validators=[DataRequired()], choices = ([(country.alpha_2, country.name) for country in pycountry.countries]))
    next        = SubmitField('Next')

class ContractDetails(FlaskForm):
    fname = StringField('First Name *', validators=[DataRequired()])
    lname = StringField('Last Name *', validators=[DataRequired()])
    job_title = StringField('Job Title', validators=[DataRequired()])
    salary = IntegerField('Salary monthly (SGD) *', validators=[DataRequired()])
    annual_leave_days = IntegerField('Number of Annual Leave Days *', validators=[DataRequired()])
    working_hours_per_week = IntegerField('Working Hours per Week (Standard 40h) *', validators=[DataRequired()])
    start_date = StringField('Employment Start Date (DD-MM-YYYY) *', validators=[DataRequired()])
    contract_duration = StringField('Contract Duration (limited / unlimited) *', validators=[DataRequired()])
    fringe_benefit = StringField('Fringe Benefit (for full time employees)', validators=[DataRequired()])
    group_insurance_coverage = StringField('Group Insurance Coverage (Management)', validators=[DataRequired()])
    special_arrangements = StringField('Special Arrangements (if any)', validators=[DataRequired()])
    send = SubmitField('Send')
