from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username', 'password')

class ClassinformationForm(forms.ModelForm):
    class Meta:
        model = Classinformation
        fields = ('ClassName', 'ClassTeacher', 'TotalStudents', 'NumberOfSections')
class EditclassinformationForm(forms.ModelForm):
    class Meta:
        model = Classinformation
        fields = ('ClassName', 'ClassTeacher', 'TotalStudents', 'NumberOfSections')

class SectioninformationForm(forms.ModelForm):
    class Meta:
        model = Sectioninformation
        fields = ('SectionTeacher','NameOfClass','NumberOfStudents', 'SectionName')
class EditsectioninformationForm(forms.ModelForm):
    class Meta:
        model = Sectioninformation
        fields = ('SectionTeacher', 'NumberOfStudents', 'SectionName')

class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('Name', 'NationaId', 'Responsibility', 'Address', 'Username', 'Password')
class EditTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('Name', 'NationaId', 'Responsibility', 'Address')

class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('Subjectname', 'Subjectcode', 'Author', 'Class', 'SubjectTeacher','Type','OtherNotes')
class EditSubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('Subjectname', 'Subjectcode', 'Author', 'Class', 'SubjectTeacher','Type','OtherNotes')

class AddSyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ('SyllabusType', 'Subject', 'Class', 'Syllabus','Notes')
class EditSyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ('SyllabusType', 'Subject', 'Class', 'Syllabus','Notes')

class AddHumanResourceForm(forms.ModelForm):
    class Meta:
        model = HumanResource
        fields = ('Name', 'NationaId', 'Designation', 'Phone','Address', 'Gender', 'Religion')
class EditHumanResourceForm(forms.ModelForm):
    class Meta:
        model = HumanResource
        fields = ('Name', 'Designation', 'Phone','Address')

class AddRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ('Class', 'Section', 'Subject', 'Day','Teacher', 'StartTime', 'EndTime','Address','RoomNumber')

class EditRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ('Class', 'Section', 'Subject', 'Day','Teacher', 'StartTime', 'EndTime','Address','RoomNumber')

class AddAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('School','AssignmentType', 'Subject', 'Class', 'Assignment','Notes')
class EditAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('School','AssignmentType', 'Subject', 'Class', 'Assignment','Notes')

class AddExamGradeForm(forms.ModelForm):
    class Meta:
        model = ExamGrade
        fields = ('School','ExamGrade', 'GradePoint', 'MarkFrom', 'MarkTo','Notes')
class EditExamGradeForm(forms.ModelForm):
    class Meta:
        model = ExamGrade
        fields = ('School','ExamGrade', 'GradePoint', 'MarkFrom', 'MarkTo','Notes')


class AddExamTermForm(forms.ModelForm):
    class Meta:
        model = ExamTerm
        fields = ('School','ExamTitle', 'StartDate','Notes')
class EditExamTermForm(forms.ModelForm):
    class Meta:
        model = ExamTerm
        fields =('School','ExamTitle', 'StartDate','Notes')
class AddExamScheduleForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ('School','Exam', 'Class', 'Subject', 'ExamDate','StartTime','EndTime','RoomNumber','Notes')
class EditExamScheduleForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ('School','Exam', 'Class', 'Subject', 'ExamDate','StartTime','EndTime','RoomNumber','Notes')

class AddExamSuggestionForm(forms.ModelForm):
    class Meta:
        model = ExamSuggestion
        fields = ('School','SuggestionTitle', 'Class', 'Subject', 'Suggestion','Notes')
class EditExamSuggestionForm(forms.ModelForm):
    class Meta:
        model = ExamSuggestion
        fields = ('School','SuggestionTitle', 'Class', 'Subject', 'Suggestion','Notes')

class AddLibraryBookForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('School','BookTitle', 'ISBN_no', 'BookId', 'Edition','Author', 'Language', 'Price', 'Quantity','BookCover')
class EditLibraryBookForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('School','BookTitle', 'ISBN_no', 'BookId', 'Edition','Author', 'Language', 'Price', 'Quantity','BookCover')


class AddVehicleForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ('School','VehicleNumber', 'VehicleModel', 'Driver', 'VehicleLicense','VehicleContact', 'Notes')
class EditVehicleForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ('School','VehicleNumber', 'VehicleModel', 'Driver', 'VehicleLicense','VehicleContact', 'Notes')

class AddRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('School','RouteTitle', 'StartRoute', 'EndRoute','Notes')
class EditRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('School','RouteTitle', 'StartRoute', 'EndRoute','Notes')

class AddHostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ('School','HostelName', 'HostType', 'Address','Notes')
class EditHostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ('School','HostelName', 'HostType', 'Address','Notes')
