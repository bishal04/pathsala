from django.contrib import admin

from .models import Student
from .models import StudentInfo
from .models import English
from .models import Maths
from .models import Science
from .models import ComputerScience
from .models import Accounts


class StudentAdmin(admin.ModelAdmin):

    list_display = ("name","dob","gender","address","telephone",)
    search_fields = ("name","address","gender",)

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ("student", "level", "section", "rollno", "Sub1", "Sub2", "Sub3", "Sub4",)


class EnglishAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


class MathsAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


class ScienceAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


class ComputerScienceAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


class AccountsAdmin(admin.ModelAdmin):
    list_display = ("student", "total_marks", "pass_marks", "marks_obtained", "remarks",)


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(English, EnglishAdmin)
admin.site.register(Maths, MathsAdmin)
admin.site.register(Science, ScienceAdmin)
admin.site.register(ComputerScience, ComputerScienceAdmin)
admin.site.register(Accounts, AccountsAdmin)
