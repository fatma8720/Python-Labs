from django import forms
from prof.models import Prof
from .models import *

class NewStudentForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    course = forms.CharField(max_length=100, required=True)
    year = forms.IntegerField(required=True)
    image = forms.ImageField()
    prof = forms.ChoiceField(choices=Prof.Get_all())

class NewStudentFormModel(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
