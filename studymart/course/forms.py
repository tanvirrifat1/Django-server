from django import forms
from . models import Student


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_email', 'batch', 'course']
        labels = {
            'student_name': 'Full Name',
            'student_email': 'Email',
            'batch': 'Batch',
            'course': 'Course'
        }
