from django.db import models
class Login(models.Model):
    username = models.CharField(max_length=130)
    password = models.CharField(max_length=30, blank=True)

class Createclassinformation(models.Model):
    ClassName = models.CharField(max_length=130)
    ClassTeacher = models.CharField(max_length=30, blank=True)
    TotalStudents = models.CharField(max_length=30, blank=True)
    NumberOfSections = models.CharField(max_length=30, blank=True)
