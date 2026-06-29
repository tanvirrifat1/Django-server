from django.shortcuts import render
from django.http import HttpResponse

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
