from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column, Layout, Div, Field, HTML
from .models import Device


class DateInput(forms.DateInput):
    input_type = 'date'


class DeviceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Div(
                Div('name', css_class='col-md-6'),
                Div('serial_number', css_class='col-md-6'),
                css_class='row',
            ),
            Div(
                Div('contract', css_class='col-md-4'),
                Div('expiration_date', type='date', css_class='col-md-4'),
                Div('renewal_date', css_class='col-md-4'),
                css_class='row',
            ),
            Div(
                Div('place', css_class='col-md-4'),
                Div('user', css_class='col-md-4'),
                css_class='row',
            ),
            Div(
                Div('make', css_class='col-md-6'),
                Div('model', css_class='col-md-6'),
                css_class='row',
            ),
            HTML("""
                    <br>
                """),
            Div(
                Submit('submit', 'Add'),
            )
        )

        # self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Device
        fields = ('__all__')
        widgets = {
            'expiration_date': DateInput(),
            'renewal_date': DateInput()
        }


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


