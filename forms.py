from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, IntegerField
import pycountry

class GeneralDetails(FlaskForm):
    fname = StringField('First Name *', validators=[DataRequired()])
    lname = StringField('Last Name *', validators=[DataRequired()])
    email = EmailField('Personal Email Address (e.g. xxxxx@gmail.com) *', validators=[DataRequired()])
    address = StringField('Address *', validators=[DataRequired()])
    city = StringField('City *', validators=[DataRequired()])
    province = StringField('Province*', validators=[DataRequired()])
    postal_code = IntegerField('Postal Code*', validators=[DataRequired()])
    country = SelectField('Country*', validators=[DataRequired()], choices=([(country.alpha_2, country.name) for country in pycountry.countries]))
    next = SubmitField('Next')

class ContractDetails(FlaskForm):
    fname = StringField('FName', validators=[DataRequired()])
    lname = StringField('LName', validators=[DataRequired()])
    job_title = StringField('Job Title', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    annual_leave_days = IntegerField('Annual Leave Days', validators=[DataRequired()])
    working_hours_per_week = IntegerField('Working Hours per Week', validators=[DataRequired()])
    start_date = StringField('Employment Start Date', validators=[DataRequired()])
    contract_duration = StringField('Contract Duration', validators=[DataRequired()])
    fringe_benefit = StringField('Fringe Benefit', validators=[DataRequired()])
    group_insurance_coverage = StringField('Group Insurance Coverage', validators=[DataRequired()])
    special_arrangements = StringField('Special Arrangements', validators=[DataRequired()])
    send = SubmitField('Send')
    back = SubmitField('Back')
