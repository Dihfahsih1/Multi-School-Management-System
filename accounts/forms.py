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

class CreateTeacherForm(forms.ModalForm):
    class Meta:
        model = Teacher
        fields = ('Name', 'NationalId', 'Responsibility', 'Address', 'Username', 'Password')
class EditTeacherForm(forms.ModalForm):
    class Meta:
        model = Teacher
        fields = ('Name', 'NationalId', 'Responsibility', 'Address')
