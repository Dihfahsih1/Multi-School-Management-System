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
        return self.SectionName
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
    Address = models.CharField(max_length=130)
    Religion = models.CharField(max_length=130)
    def __str__(self):
        return self.Name

class Routine(models.Model):
    choices = (('Monday','Monday'), ('Tuesday', 'Tuesday'),
     ('Wednesday','Wednesday'), ('Thursday', 'Thursday'),
     ('Friday','Friday'), ('Saturday', 'Saturday'),
     ('Sunday','Sunday'))
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Section = models.ForeignKey(Sectioninformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Day = models.CharField(max_length=10, choices=choices, blank=False, null=True)
    Teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True, null=True)
    StartTime = models.CharField(max_length=130, default="11:30 AM")
    EndTime = models.CharField(max_length=130, default="1:30 PM")
    Address = models.CharField(max_length=130)
    RoomNumber = models.CharField(max_length=130)

class Assignment(models.Model):
    School = models.CharField(max_length=130)
    AssignmentType = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Deadline =models.CharField(max_length=130, blank=False)
    Assignment = models.FileField(max_length=130, blank=False)
    Notes = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.Assignment

class ExamGrade(models.Model):
    School = models.CharField(max_length=130)
    ExamGrade =  models.CharField(max_length=130)
    GradePoint = models.CharField(max_length=130)
    MarkFrom = models.CharField(max_length=130)
    MarkTo = models.CharField(max_length=130)
    Notes =  models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.ExamGrade

class ExamTerm(models.Model):
    School = models.CharField(max_length=130)
    ExamTitle =  models.CharField(max_length=130)
    StartDate = models.CharField(max_length=130)
    Notes =  models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.ExamTitle
