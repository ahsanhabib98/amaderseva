from django import forms
from .models import *
from django.forms import TextInput, Textarea, Select


class MobilePhoneForm(forms.ModelForm):
    class Meta:
        model = MobilePhone
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'condition': Select(attrs={'class':'form-control'}),
            'brand': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
            'model': TextInput(attrs={'class':'form-control'}),
            'price': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
        }


class ComputingForm(forms.ModelForm):
    class Meta:
        model = Computing
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'condition': Select(attrs={'class':'form-control'}),
            'brand': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
            'model': TextInput(attrs={'class':'form-control'}),
            'configuration': TextInput(attrs={'class':'form-control'}),
            'price': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
        }

class TelevisionForm(forms.ModelForm):
    class Meta:
        model = Television
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'condition': Select(attrs={'class':'form-control'}),
            'brand': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
            'model': TextInput(attrs={'class':'form-control'}),
            'price': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
        }


class OthersForm(forms.ModelForm):
    class Meta:
        model = Others
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'condition': Select(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
            'price': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
        }


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'bed': TextInput(attrs={'class':'form-control'}),
            'bathroom': TextInput(attrs={'class':'form-control'}),
            'flat_area': TextInput(attrs={'class':'form-control'}),
            'address': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
            'price': TextInput(attrs={'class':'form-control'}),
            'title': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
        }

class EcommerceForm(forms.ModelForm):
    class Meta:
        model = Ecommerce
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
            'price': TextInput(attrs={'class':'form-control'}),
            'warrenty': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'study_item': Select(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
            'price': TextInput(attrs={'class':'form-control'}),
            'warrenty': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
        }
