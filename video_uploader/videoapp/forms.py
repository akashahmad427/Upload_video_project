
from .models import Video
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class Newform(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        labels = {'video_file':''}

class Fistform(UserCreationForm):
    password2 = forms.CharField(label='Conform password (again)',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'email'}
