from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from django import forms
from .models import Student

class StudentInfoForm(ModelForm):
    class Meta:
        model = Student
        fields = ['libid', 'email', 'name', 'course', 'branch', 'year', 'phone', 'address', 'password']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                })
        }
    name = forms.CharField(max_length=50, required=True, widget=Meta.widgets['name'])
    email = forms.EmailField(required=True)
    libid = forms.IntegerField(required=True)
    course = forms.CharField(max_length=20, required=True)
    branch = forms.CharField(max_length=20, required=True)
    year = forms.IntegerField(required=True)
    phone = forms.IntegerField(required=True)
    address = forms.CharField(widget=forms.Textarea)
    password = forms.PasswordInput()
