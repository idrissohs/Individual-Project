from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Idea


#form to collect user data
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#form to collect project data
class IdeaForm (ModelForm): 
    
    class Meta:
        model = Idea
        fields = ['title', 'about', 'domain', 'tags']
