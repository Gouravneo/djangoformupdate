from django import forms
from .models import Studyprogram

class StudentForm(forms.ModelForm):
    class Meta:
        model = Studyprogram
        fields=['first_name','gender','age','email','passwd']
    