from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('myProfile', views.myProfile, name='myProfile'),

]