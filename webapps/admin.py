from django.contrib import admin

from .models import Student
from .models import StudentInfo

class StudentAdmin(admin.ModelAdmin):

    list_display = ("name","dob","gender","address","telephone",)
    search_fields = ("name","address","gender",)

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ("student", "level", "section", "rollno",)




admin.site.register(Student, StudentAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
# Register your models here.
