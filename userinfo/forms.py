from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Select, Textarea
from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user','slug', ]

        widgets = {
            'profile_name': TextInput(attrs={'class':'form-control'}),
            'title': Select(attrs={'class':'form-control'}),
            'gender': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
            'birth_day': TextInput(attrs={'class':'form-control'}),
            'phone': TextInput(attrs={'class':'form-control'}),
            'qualification': Textarea(attrs={'class':'form-control'}),
        }
