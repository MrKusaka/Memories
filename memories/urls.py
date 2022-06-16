from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginFormView.as_view(), name='home'),
    path('myProfile', views.MyProfile.as_view(), name='myProfile'),
]
