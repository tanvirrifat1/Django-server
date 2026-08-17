from django.contrib import admin

# Register your models here.

from . models import Teacher

@admin.register(Teacher)

class techAdmin(admin.ModelAdmin):
    list_display=['teacher_name','teacher_reg','user']