from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username', 'password')

class Createclassinformation(forms.ModelForm):
    class Meta:
        model = Createclassinformation
        fields = ('ClassName', 'ClassTeacher', 'TotalStudents', 'NumberOfSections')        
