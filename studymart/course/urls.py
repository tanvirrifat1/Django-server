from django.urls import path
from . import views

urlpatterns = [
    path("fr", views.free_course),
    path("st", views.student_info),
    path('from/', views.show_form)
]
