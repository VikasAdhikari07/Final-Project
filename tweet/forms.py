from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class blog_form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['heading','text','photo']


class RegsitrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']