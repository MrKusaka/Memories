import vk
from django.views.generic.edit import FormView
from django.conf import settings

from memories.forms import LoginForm, MakeMemory
from .models import Memory


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


class MyProfile(FormView):
    template_name = 'memories/myProfile.html'
    form_class = MakeMemory
    success_url = 'myProfile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api_key_yandex'] = getattr(settings, "API_KEY_YANDEX", "7c1e4364-08b4-4ec3-b1e8-dc0369119139")
        context['memories'] = Memory.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)
