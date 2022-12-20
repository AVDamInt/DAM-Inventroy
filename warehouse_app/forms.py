from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit, Row, Column, Layout, Div, Field, HTML
from .models import Device, Place, DeviceUser


class DateInput(forms.DateInput):
    input_type = 'date'


class DeviceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Div(
                Div('user_history', css_class='col-md-4'),
                Div('serial_number', css_class='col-md-4'),
                Div('status', css_class='col-md-4'),
                css_class='row',
            ),
            Div(
                Div('contract', css_class='col-md-4'),
                Div('expiration_date', type='date', css_class='col-md-4'),
                Div('renewal_date', type='date', css_class='col-md-4'),
                css_class='row',
            ),
            Div(
                Div('place', css_class='col-md-6'),
                Div('user', css_class='col-md-6'),
                css_class='row',
            ),
            Div(
                Div('make', css_class='col-md-6'),
                Div('model', css_class='col-md-6'),
                css_class='row',
            ),
            HTML("""
                    <br>
                """)
        )
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            'expiration_date': DateInput(),
            'renewal_date': DateInput()
        }


class DeviceUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Div(
                Div('user_history', css_class='col-md-4'),
                Div('serial_number', css_class='col-md-4'),
                Div('status', css_class='col-md-4'),
                css_class='row',
            ),
            Div(
                Div('contract', css_class='col-md-4'),
                Div('expiration_date', type='date', css_class='col-md-4'),
                Div('renewal_date', type='date', css_class='col-md-4'),
                css_class='row',
            ),
            Div(
                Div('place', css_class='col-md-6'),
                Div('user', css_class='col-md-6'),
                css_class='row',
            ),
            Div(
                Div('make', css_class='col-md-6'),
                Div('model', css_class='col-md-6'),
                css_class='row',
            ),
            HTML("""
                    <br>
                """)
        )

        self.helper.add_input(Submit('submit', 'Edit'))

    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            'expiration_date': DateInput(),
            'renewal_date': DateInput()
        }


class PlaceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'place_register'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('country', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('city', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('address', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('cap', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('plan', css_class='col-md-4'),
                css_class='form-row',
            ),
            HTML("""
                    <br>
                """)
        )
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Place
        fields = '__all__'


class PlaceUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlaceUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        # self.helper.form_action = 'place_register'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('country', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('city', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('address', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('cap', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('plan', css_class='col-md-4'),
                css_class='form-row',
            ),
            HTML("""
                    <br>
                """)
        )
        self.helper.add_input(Submit('submit', 'Edit'))

    class Meta:
        model = Place
        fields = '__all__'


class DeviceUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('surname', css_class='col-sm-4 col-sm-offset-4'),
                css_class='form-row',
            ),
            Row(
                Column('email', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('role', css_class='col-md-4'),
                css_class='form-row',
            ),
            HTML("""
                    <br>
                """)

        )
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = DeviceUser
        fields = '__all__'


class DeviceUserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceUserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('surname', css_class='col-sm-4 col-sm-offset-4'),
                css_class='form-row',
            ),
            Row(
                Column('email', css_class='col-md-4'),
                css_class='form-row',
            ),
            Row(
                Column('role', css_class='col-md-4'),
                css_class='form-row',
            ),
            HTML("""
                    <br>
                """)
        )
        self.helper.add_input(Submit('submit', 'Edit'))

    class Meta:
        model = DeviceUser
        fields = '__all__'


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
