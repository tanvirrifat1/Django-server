from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . forms import StudentRegistration

# Create your views here.


def free_course(request):
    course1 = "free course"
    course2 = "paid course"
    course3 = "free course"
    course4 = "paid course"
    course_details = {
        "c1": course1,
        "c2": course2,
        "c3": course3,
        "c4": course4,
    }
    return render(request, "resources/free_course.html", course_details)

def student_info(request):
    sdetails=Student.objects.all()
    return render(request, "courses/student_info.html", {"student_details": sdetails})



def show_form(req):
    frm = StudentRegistration()
    frm.order_fields(field_order=['email','first_name','last_name','batch'])
    return render(req, 'courses/forms.html', {'form': frm})