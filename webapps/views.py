from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

def get_all_student(request):
    students = Student.objects.all()


    return render(request, "list_students.html", context={"students": students})


def get_student(request, webapps_std_id):
    
    student = Student.objects.get(pk=webapps_std_id)
    

    return render(request,  "get_students.html", context={"student": student})
