from django.shortcuts import render, redirect
from .models import Task
import requests
import vk
import vk_api
import json


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'memories/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


# def auth_vk_password():
#     session = vk.AuthSession(app_id=APP_ID,
#                              user_login=input("user_login: "),
#                              user_password=input("user_password: "))
#     file = open("auth_vk.ini", 'w')
#     file.writelines(session.access_token)
#     return session


def myProfile(request):
    f = open('C:\\Users\\wow_l\\PycharmProjects\\djangoProject\\memories\\keys.json')
    api_key = json.load(f)
    return render(request, 'memories/myProfile.html', {'api_key_yandex': api_key['api_key_yandex']})

