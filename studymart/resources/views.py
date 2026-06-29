from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def free_course(request):
    return render(request, "blog.html")
