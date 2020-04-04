from src.service.dynamic_form import dynamic_form, FIELD_TYPE


class Test:

    def test(self):
        fields =     {
            'some_int': FIELD_TYPE.int,
            'some_str': FIELD_TYPE.str,
        }
        form_name = 'demo_dynamic_form'
        dynamic_form(fields, form_name)
