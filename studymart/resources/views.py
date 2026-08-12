from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def free_course(request):
    return render(request, "blog.html")


def userfrom(request):


    if request.method == "POST":
        frm=UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()

    else:
        frm=UserCreationForm()

    frm=UserCreationForm()
    return render(request, "resources/userfrom.html", {"form": frm})
     