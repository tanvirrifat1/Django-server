from django import forms
from .models import Student


class StudentRegistration(forms.Form):
    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=50, label="Last Name")
    email = forms.EmailField(max_length=100, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    batch = forms.IntegerField(label="Batch")
    textarea = forms.CharField(widget=forms.Textarea, required=False, label="Textarea")
    payment = forms.CharField(max_length=50, label="Payment")
    django = forms.CharField(max_length=50, label="Django")

    def save(self, commit=True):
        student = Student(
            student_name=f"{self.cleaned_data['first_name']} {self.cleaned_data['last_name']}",
            student_email=self.cleaned_data['email'],
            batch=self.cleaned_data['batch'],
            course=self.cleaned_data['payment'],
        )
        if commit:
            student.save()
        return student
