from django.contrib import admin

from .models import Student
from .models import StudentInfo
from .models import English
from .models import Math
from .models import Science
from .models import ComputerScience
from .models import Account
from .models import Teacher


class StudentAdmin(admin.ModelAdmin):

    list_display = ("name","dob","gender","address","telephone",)
    search_fields = ("name","address","gender",)

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ("student", "level", "section", "rollno", "Sub1", "Sub2", "Sub3", "Sub4",)


class EnglishAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


class MathAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


class ScienceAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


class ComputerScienceAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


class AccountAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "telephone", "subject",)


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(English, EnglishAdmin)
admin.site.register(Math, MathAdmin)
admin.site.register(Science, ScienceAdmin)
admin.site.register(ComputerScience, ComputerScienceAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Teacher, TeacherAdmin)
