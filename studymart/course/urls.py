from django.urls import path
from . import views

urlpatterns = [
    path("fr", views.free_course, name="free_course"),
    path("st", views.student_info, name="student_info"),
    path("from/", views.show_form, name="show_form"),
    path("success/", views.show_success, name="success"),
]
