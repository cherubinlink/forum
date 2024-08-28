from django.forms import ModelForm
from django import forms
from .models import User



class UserForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email']



