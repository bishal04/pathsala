from django.db import models



class Student(models.Model):
    std_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    dob = models.DateField(verbose_name="Date Of Birth")
    gender = models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")),default='F')
    address = models.TextField()
    telephone = models.CharField(max_length=15)

def __repr__(self):
    return self.name

__str__ = __repr__

class StudentInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name="student")
    level = models.IntegerField()
    section = models.CharField(max_length=1)
    rollno = models.IntegerField()
    
  