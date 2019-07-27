from django.db import models
class Login(models.Model):
    username = models.CharField(max_length=130)
    password = models.CharField(max_length=30, blank=True)

class Classinformation(models.Model):
    ClassName = models.CharField(max_length=130)
    ClassTeacher = models.CharField(max_length=30, blank=True)
    TotalStudents = models.CharField(max_length=30, blank=True)
    NumberOfSections = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return 'Class Name:{0} Students Number:{1}'.format(self.ClassName, self.TotalStudents)

class Sectioninformation(models.Model):
    NameOfClass = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    SectionName = models.CharField(max_length=130)
    SectionTeacher = models.CharField(max_length=30, blank=True)
    NumberOfStudents = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.NameOfClass
