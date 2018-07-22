from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
from .models import Teacher

def get_all_student(request):
    students = Student.objects.all()


    return render(request, "list_students.html", context={"students": students})


def get_student(request, webapps_std_id):
    
    student = Student.objects.get(pk=webapps_std_id)
    

    return render(request,  "get_students.html", context={"student": student})


def get_all_teacher(request):
    teachers = Teacher.objects.all()

    return render(request, "list_teachers.html", context={"teachers": teachers})
    

def get_teacher(request, webapps_teacher_id):
    teacher = Teacher.objects.get(pk=webapps_teacher_id)

    return render(request, "get_teachers.html", context={"teacher": teacher})
    