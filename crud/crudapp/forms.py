from django.forms import ModelForm
from django import forms
from crudapp.models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
