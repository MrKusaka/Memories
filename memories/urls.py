from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginFormView.as_view(), name='home'),
    path('myProfile', views.myProfile, name='myProfile'),
]
