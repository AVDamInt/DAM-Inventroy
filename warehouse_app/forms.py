from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit, Row, Column, Layout, Div, HTML, Field
from .models import Device, Place, DeviceUser, Department, Office, Company


class DateInput(forms.DateInput):
    input_type = "date"


class DepartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = "department_register"
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-2"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Add"))

    class Meta:
        model = Department
        fields = "__all__"


class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = "company_register"
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-2"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Add"))

    class Meta:
        model = Company
        fields = "__all__"


class CompanyUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-4"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Edit"))

    class Meta:
        model = Company
        fields = "__all__"


class OfficeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OfficeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = "office_register"
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-2"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Add"))

    class Meta:
        model = Office
        fields = "__all__"


class OfficeUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OfficeUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-4"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Edit"))

    class Meta:
        model = Office
        fields = "__all__"


class DepartmentUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DepartmentUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-4"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Edit"))

    class Meta:
        model = Department
        fields = "__all__"


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = "__all__"
        widgets = {
            "expiration_date": DateInput(format="%d/%m/%Y"),
            "renewal_date": DateInput(format="%d/%m/%Y")
        }

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Div(
                Div("company", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("host_name", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("serial_number", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("status", css_class="col-md-4"),
                css_class="row",
            ),
            Div(
                Div("contract", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("expiration_date", type="date", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("renewal_date", type="date", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("place", css_class="col-md-2"),
                Div("department", css_class="col-md-2"),
                Div("office", css_class="col-md-2"),
                css_class="row"
            ),
            Div(
                Div("user_history", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("history_type", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("phase", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("user", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("make", css_class="col-md-2"),
                Div("model", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("cpu", css_class="col-md-2"),
                Div("addr_ip", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("memory", css_class="col-md-2"),
                Div("memory_unit", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("hard_disk", css_class="col-md-2"),
                Div("hard_disk_unit", css_class="col-md-2"),
                css_class="row",
            ),

            Div(
                Div("note", css_class="col-md-2"),
                css_class="row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Add"))


class DeviceUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Div(
                Div("host_name", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("serial_number", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("status", css_class="col-md-4"),
                css_class="row",
            ),
            Div(
                Div("contract", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("expiration_date", type="date", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("renewal_date", type="date", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                css_class="row",
            ),
            Div(
                Div("place", css_class="col-md-2"),
                Div("user", css_class="col-md-2"),
                Div("user_history", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("make", css_class="col-md-2"),
                Div("model", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("cpu", css_class="col-md-2"),
                Div("addr_ip", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("memory", css_class="col-md-2"),
                Div("memory_unit", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("hard_disk", css_class="col-md-2"),
                Div("hard_disk_unit", css_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Div("note", css_class="col-md-2"),
                css_class="row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Edit"))

    class Meta:
        model = Device
        fields = "__all__"
        widgets = {"expiration_date": DateInput(), "renewal_date": DateInput()}


class PlaceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_action = "place_register"
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-2"),
                css_class="form-row",
            ),
            Row(
                Column("country", css_class="col-md-2"),
                css_class="form-row",
            ),
            Row(
                Column("city", css_class="col-md-2"),
                css_class="form-row",
            ),
            Row(
                Column("address", css_class="col-md-2"),
                css_class="form-row",
            ),
            Row(
                Column("cap", css_class="col-md-2"),
                css_class="form-row",
            ),
            Row(
                Column("plan", css_class="col-md-2"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Add"))

    class Meta:
        model = Place
        fields = "__all__"


class PlaceUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlaceUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = 'place_register'
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-4"),
                css_class="form-row",
            ),
            Row(
                Column("country", css_class="col-md-4"),
                css_class="form-row",
            ),
            Row(
                Column("city", css_class="col-md-4"),
                css_class="form-row",
            ),
            Row(
                Column("address", css_class="col-md-4"),
                css_class="form-row",
            ),
            Row(
                Column("cap", css_class="col-md-4"),
                css_class="form-row",
            ),
            Row(
                Column("plan", css_class="col-md-4"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Edit"))

    class Meta:
        model = Place
        fields = "__all__"


class DeviceUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-4"),
                css_class="form-row",
            ),
            Row(
                Column("surname", css_class="col-sm-4"),
                css_class="form-row",
            ),
            Row(
                Column("email", css_class="col-md-4"),
                css_class="form-row",
            ),
            Row(
                Column("department", css_class="col-md-4"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Add"))

    class Meta:
        model = DeviceUser
        fields = "__all__"


class DeviceUserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceUserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        # self.helper.form_action = 'device_register'
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-4"),
                css_class="form-row",
            ),
            Row(
                Column("surname", css_class="col-sm-4 col-sm-offset-4"),
                css_class="form-row",
            ),
            Row(
                Column("email", css_class="col-md-4"),
                css_class="form-row",
            ),
            Row(
                Column("role", css_class="col-md-4"),
                css_class="form-row",
            ),
            HTML(
                """
                    <br>
                """
            ),
        )
        self.helper.add_input(Submit("submit", "Edit"))

    class Meta:
        model = DeviceUser
        fields = "__all__"


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()

    def clean(self):
        cleaned_data = super(UploadFileForm, self).clean()
        file = cleaned_data.get('file')

        if file:
            filename = file.name
            print(filename)
            if filename.endswith('.xlsx'):
                print
                'File is an excel'
            else:
                print
                'File is NOT an excel'
                raise forms.ValidationError("File is not a excel. Please upload only mp3 files")

        return file
