from django import forms


class StudentRegistration:
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    batch = forms.IntegerField()
