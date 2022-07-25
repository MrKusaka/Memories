from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

from .models import Memory


class LoginForm(forms.Form):
    login = forms.CharField(label='Логин:')
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput())

    # def __init__(self, request):
    #     super().__init__(self)
    #     self.request = request

    def clean(self):
        username = self.cleaned_data['login']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("Неправильный логин или пароль")


class MakeMemory(forms.ModelForm):
    comments = forms.CharField(label='Комментарий:', widget=forms.Textarea())
    latitude = forms.FloatField(label='', widget=forms.HiddenInput())
    longitude = forms.FloatField(label='', widget=forms.HiddenInput())

    class Meta:
        model = Memory
        fields = '__all__'


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']