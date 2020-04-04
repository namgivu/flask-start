from src.service.dynamic_form import dynamic_form, FIELD_TYPE

class Test:
    def test(self):
        fields = {
            'First Name': FIELD_TYPE.str,
            'Last Name': FIELD_TYPE.str,
            'Email': FIELD_TYPE.email,
            'Address': FIELD_TYPE.str,
            'City': FIELD_TYPE.str,
            'Province': FIELD_TYPE.str,
            'Postal Code': FIELD_TYPE.int,
            'Country': FIELD_TYPE.str,
            'Job Title' : FIELD_TYPE.str,
            'Contract Duration' : FIELD_TYPE.str,
            'Next': FIELD_TYPE.submit
        }
        form_name = 'demo_dynamic_form'
        dynamic_form(fields, form_name)
