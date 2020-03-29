from flask import *
from src.forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '2b90d6706f3dcb6919c351822ec0dc11'


@app.route('/')
def hi():
   return 'Hi there!'

@app.route('/form1', methods=['GET', 'POST'])
def form1():
   form = GeneralDetails()
   if request.method == 'POST':
      data = dict(
         fname=form.fname.data,
         lname=form.lname.data,
         email=form.email.data,
         address=form.address.data,
         city=form.city.data,
         province=form.province.data,
         postal_code=form.postal_code.data,
         country=form.country.data
      )
      print(data)
      return redirect(url_for('form2'))
   return render_template('form1.html', form=form)

@app.route('/form2')
def form2():
   form = ContractDetails
   return render_template('form2.html', form=form)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)
