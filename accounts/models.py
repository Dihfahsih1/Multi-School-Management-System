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
        return self.ClassName

class Sectioninformation(models.Model):
    NameOfClass = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    SectionName = models.CharField(max_length=130)
    SectionTeacher = models.CharField(max_length=30, blank=True)
    NumberOfStudents = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.NameOfClass
class Teacher(models.Model):
    Name = models.CharField(max_length=130)
    NationaId = models.CharField(max_length=130)
    Responsibility = models.CharField(max_length=130)
    Address = models.CharField(max_length=130)
    Username = models.CharField(max_length=130)
    Password = models.CharField(max_length=130)

    def __str__(self):
        return self.Name

class Subjects(models.Model):
    choices = (
    ('Compulsory','Compulsory'),('Options','Options')
    )
    Subjectname = models.CharField(max_length=130)
    Subjectcode = models.CharField(max_length=130)
    Author = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    SubjectTeacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True, null=True)
    Type = models.CharField(max_length=130, choices=choices, blank=False)
    OtherNotes = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.Subjectname

class Syllabus(models.Model):
    SyllabusType = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Syllabus = models.FileField(max_length=130, blank=False)
    Notes = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.Syllabus

class HumanResource(models.Model):
    choices = (('female','female'), ('male', 'male'))
    Name = models.CharField(max_length=130)
    NationaId = models.CharField(max_length=130)
    Designation = models.CharField(max_length=130)
    Phone = models.CharField(max_length=130)
    Gender = models.CharField(max_length=10, choices=choices, blank=False, null=True)
    Adress = models.CharField(max_length=130)
    Religion = models.CharField(max_length=130)
