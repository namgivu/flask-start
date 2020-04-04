from flask import *
from src.forms import *
import src.service.mongo as MongoSvc
from src.dynamic_form.demo_dynamic_form import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '2b90d6706f3dcb6919c351822ec0dc11'
app.static_folder = 'static'

@app.route('/success')
def hi():
   return render_template('success.html')

@app.route('/form1', methods=['GET', 'POST'])
def form1():
   form = GeneralDetails()
   if request.method == 'POST':
      data = dict(
         first_name        = form.fname.data,
         last_name         = form.lname.data,
         email             = form.email.data,
         address           = form.address.data,
         city              = form.city.data,
         province          = form.province.data,
         postal_code       = form.postal_code.data,
         country           = form.country.data
      )
      MONGO_TEST_COLLECTION = 'form1'
      MongoSvc.insert(data, MONGO_TEST_COLLECTION)
      return redirect(url_for('form2'))
   return render_template('form1.html', form=form)

@app.route('/form2', methods=['GET', 'POST'])
def form2():
   form = ContractDetails()
   if request.method == 'POST':
      data = dict(
         first_name               = form.fname.data,
         last_name                = form.lname.data,
         job_title                = form.job_title.data,
         salary                   = form.salary.data,
         annual_leave_days        = form.annual_leave_days.data,
         working_hours_per_week   = form.working_hours_per_week.data,
         start_date               = form.start_date.data,
         contract_duration        = form.contract_duration.data,
         fringe_benefit           = form.fringe_benefit.data,
         group_insurance_coverage = form.group_insurance_coverage.data,
         special_arrangements     = form.special_arrangements.data
      )
      MONGO_TEST_COLLECTION = 'form2'
      MongoSvc.insert(data, MONGO_TEST_COLLECTION)
      return redirect(url_for('hi'))

   return render_template('form2.html', form=form)

@app.route('/dynamic_form', methods=['GET', 'POST'])
def dynamic_form():
   form = demo_dynamic_form()
   if request.method == 'POST':
      data = dict(
         First_Name                 = form.First_Name.data,
         Last_Name                  = form.Last_Name.data,
         Email                      = form.Email.data,
         Address                    = form.Address.data,
         City                       = form.City.data,
         Province                   = form.Province.data,
         Postal_Code                = form.Postal_Code.data,
         Country                    = form.Country.data,
         Job_Title                  = form.Job_Title.data,
         Contract_Duration          = form.Contract_Duration.data
      )
      return data

   return render_template('dynamic_form/demo_dynamic_form.html', form=form)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)
