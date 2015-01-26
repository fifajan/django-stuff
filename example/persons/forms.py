from django import forms

class AddPersonForm(forms.Form):
    short_name = forms.CharField(max_length=32, required=True)
    full_name = forms.CharField(max_length=128, required=False)
    email = forms.EmailField(max_length=128, required=False)

class RemovePersonForm(forms.Form):
    short_name_substr = forms.CharField(max_length=32, required=True)
