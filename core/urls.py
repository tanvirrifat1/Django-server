from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cr/", include("course.urls")),
    path("res/", include("resources.urls")),
]
