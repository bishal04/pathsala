from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):

    list_display = ("name","dob","gender","address","telephone",)
    search_fields = ("name","address","gender",)

admin.site.register(Student, StudentAdmin)
# Register your models here.
