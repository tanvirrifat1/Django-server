from django.urls import path
from . import views

urlpatterns = [
    path("fr", views.free_course),
    path("userform/", views.userfrom, name="userfrom"),
]
