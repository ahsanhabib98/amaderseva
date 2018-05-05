from django import forms
from django.forms import TextInput, Textarea
from .models import *



class ContactForm(forms.Form):
    # name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

class MessangerForm(forms.ModelForm):
    class Meta:
        model = Messanger
        fields = '__all__'
        exclude = ['user', 'profile', ]

class CommentMobilePhoneForm(forms.ModelForm):
    class Meta:
        model = CommentMobilePhone
        exclude = ['service',]

class CommentComputingForm(forms.ModelForm):
    class Meta:
        model = CommentComputing
        exclude = ['service',]

class CommentTelevisionForm(forms.ModelForm):
    class Meta:
        model = CommentTelevision
        exclude = ['service',]

class CommentOthersForm(forms.ModelForm):
    class Meta:
        model = CommentOthers
        exclude = ['service',]

class CommentApartmentForm(forms.ModelForm):
    class Meta:
        model = CommentApartment
        exclude = ['service',]

class CommentEcommerceForm(forms.ModelForm):
    class Meta:
        model = CommentEcommerce
        exclude = ['service',]

class CommentEducationForm(forms.ModelForm):
    class Meta:
        model = CommentEducation
        exclude = ['service',]
