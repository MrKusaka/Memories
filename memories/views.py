import json

from django.shortcuts import render
from .models import Task
import vk
from django.views.generic.edit import FormView
from memories.forms import LoginForm
from django.conf import settings


class LoginFormView(FormView):
    template_name = 'memories/index.html'
    form_class = LoginForm
    success_url = 'myProfile'

    def auth_vk_password(self, login, password):
        session = vk.AuthSession(app_id=settings.APP_ID,
                                 user_login=login,
                                 user_password=password)
        file = open("auth_vk.ini", 'w')
        file.writelines(session.access_token)
        return session

    def form_valid(self, form):
        self.auth_vk_password(form.cleaned_data['login'], form.cleaned_data['password'])
        return super().form_valid(form)


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'memories/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def myProfile(request):
    with open(str(settings.BASE_DIR) + '\\memories\\keys.json', "r") as f:
        return render(request, 'memories/myProfile.html', {'api_key_yandex': json.load(f)['api_key_yandex']})
