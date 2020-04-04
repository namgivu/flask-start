import datetime as datetime
from wtforms import IntegerField, StringField


class FIELD_TYPE:
    int=IntegerField
    str=StringField
    datetime=datetime


def dynamic_form(fields:dict, form_name:str):
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
