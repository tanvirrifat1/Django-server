from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import usercf

# Create your views here.


def free_course(request):
    return render(request, "blog.html")


def userfrom(request):


    if request.method == "POST":
        frm=usercf(request.POST)
        if frm.is_valid():
            frm.save()

    else:
        frm=usercf()

    return render(request, "resources/userfrom.html", {"form": frm})
     