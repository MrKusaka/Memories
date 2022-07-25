import vk
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages

from memories.forms import LoginForm, MakeMemory, UserRegistrationForm
from .models import Memory
from django.contrib.auth.forms import UserCreationForm


class LoginFormView(FormView):
    template_name = 'memories/index.html'
    form_class = LoginForm
    success_url = 'myProfile'

    def form_valid(self, form):
        print(self.__dict__, form.__dict__)
        username = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


# ----------Будущая реализация входа через соц. сеть - вк-----------------
# def auth_vk_password(self, login, password):
#     session = vk.AuthSession(app_id=settings.APP_ID,
#                              user_login=login,
#                              user_password=password)
#     file = open("auth_vk.ini", 'w')
#     file.writelines(session.access_token)
#     return session

# def form_valid(self, form):
#     self.auth_vk_password(form.cleaned_data['login'], form.cleaned_data['password'])
#     return super().form_valid(form)


class MyProfile(FormView):
    template_name = 'memories/myProfile.html'
    form_class = MakeMemory
    success_url = 'myProfile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api_key_yandex'] = settings.API_KEY_YANDEX
        context['memories'] = Memory.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'memories/register.html', {'user_form': user_form})
