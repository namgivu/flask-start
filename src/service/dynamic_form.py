import os

root_path = os.path.abspath(__file__ + "/../../..")

class FIELD_TYPE:
    int='IntegerField'
    str='StringField'
    submit='SubmitField'
    email='EmailField'


def dynamic_form(fields, form_name):
    # create {form_name}.py file
    form = open(f'{root_path}/src/dynamic_form/{form_name}.py', 'w')
    form.write(f'''from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, IntegerField

class {form_name}(FlaskForm):
    ''')
    for key, value in fields.items():
        form.write(f'''{key.replace(' ', '_')} = {value}('{key}', validators=[DataRequired()])''' + '\n    ')
    form.close()

    #create {form_name}.html file
    html = open(f'{root_path}/src/templates/dynamic_form/{form_name}.html', 'w')
    html.write(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link type="text/css" rel="stylesheet" href="{{{{ url_for('static', filename='style.css') }}}}">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Title</title>
</head>
<body>
    <div class="container">
        <h2 class="title">{form_name}</h2>
        <br>
        <form method="post" action="">
            {{{{ form.hidden_tag() }}}}''')
    for key, value in fields.items():
        if value == 'SubmitField':
            html.write(f'''
                    <fieldset class="form-group">
                        {{{{ form.{key.replace(' ', '_')}(class="btn btn-success") }}}}
                    </fieldset>
            ''')
        else:
            html.write(f'''
                    <fieldset class="form-group">
                        {{{{ form.{key.replace(' ', '_')}.label }}}}
                        {{{{ form.{key.replace(' ', '_')}(class="form-control") }}}}
                    </fieldset>
            ''')


    html.write('''
            </form>
    </div>
</body>
</html>
''')
    html.close()

    """
    **sample input**
    fields =     {
        'some_int': FIELD_TYPE.int,
        'some_str': FIELD_TYPE.str,
    }

    **output**
    create
        :flask-start/src/               dynamic_form/:form_name.py
        :flask-start/src/templates/     dynamic_form/:form_name.html
    that will help to operate as same thing as Trang 's form1, form2

    **steps breakdown**
    step            detail
    ---------------------------------------------------------------------------------
    create1         create class :FormName:
                        some_int = XXXField()
                        some_str = XXXField()
                        ...

    create2         create :form_name.html
                    take template similar to form1/form2

    aftermath       (manually run)
                    form = :FormName()
                    return render_template(':form_name.html', form=form)

    ** coding hints **
    for fn, ft in fields.items() :
        # create form_name.py
        '''
        class FormName:
            fn: {ft}('fn', ...)
        '''

        # create form_name.html
        ...
    """
