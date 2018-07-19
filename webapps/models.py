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
    Sub1 = models.CharField(max_length=20, choices=(("E", "English"), ("M", "Math"), ("S", "Science"), ("C", "ComputerScience"),("A", "Accounts")), default='select subject')
    Sub2 = models.CharField(max_length=20, choices=(("E", "English"), ("M", "Math"), ("S", "Science"), ("C", "ComputerScience"),("A", "Accounts")), default='select subject')
    Sub3 = models.CharField(max_length=20, choices=(("E", "English"), ("M", "Math"), ("S", "Science"), ("C", "ComputerScience"),("A", "Accounts")), default='select subject')
    Sub4 = models.CharField(max_length=20, choices=(("E", "English"), ("M", "Math"), ("S", "Science"), ("C", "ComputerScience"),("A", "Accounts")), default='select subject')
    Sub4 = models.CharField(max_length=20, choices=(("E", "English"), ("M", "Math"), ("S", "Science"), ("C", "ComputerScience"),("A", "Accounts")), default='select subject')




class English(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="student", default=0)
    total_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField()

class Maths(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="student", default=0)
    total_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField()

class Science(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="student", default=0)
    total_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField()          

class ComputerScience(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="student", default=0)
    total_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField()    

class Accounts(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="student", default=0)
    total_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField()

 