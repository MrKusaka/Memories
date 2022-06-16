from django import forms

from .models import Memory


class LoginForm(forms.Form):
    login = forms.CharField(label='Логин:')
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput())


class MakeMemory(forms.ModelForm):
    comments = forms.CharField(label='Комментарий:', widget=forms.Textarea())
    latitude = forms.FloatField(label='', widget=forms.HiddenInput())
    longitude = forms.FloatField(label='', widget=forms.HiddenInput())

    class Meta:
        model = Memory
        fields = '__all__'
