from django.db import models
from quickstart.enums import Role,Branches,Grades
# Create your models here.

class Teacher(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=10, null=False, blank=False, default=Role.NORMAL, choices=Role.CHOICES)
    
    def students(self):
        return self.student_set.all()


class Department(models.Model):
    head = models.OneToOneField(Teacher, on_delete=models.CASCADE, primary_key=True)
    branch_name = models.CharField(max_length=30, null=False, blank=False, default=Branches.COMPUTER, choices=Branches.CHOICES, unique=True)
     
    def students(self):
        return self.student_set.all()
 
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(null=False, blank=False, default=0)
    roll_no = models.IntegerField(null=False, blank=False, default=0)
    sec = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=20)
    marks = models.FloatField(null=False, blank=False, default=0)

class ReportCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    grade = models.CharField(max_length=10, null=False, blank=False, default=Grades.FIRST, choices=Grades.CHOICES)
    total_marks = models.IntegerField(null=False, blank=False, default=0)
    percentage = models.FloatField(null=False, blank=False, default=0)
    remarks = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)
   


