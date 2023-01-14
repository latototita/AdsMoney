from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    
    path('', index, name='index'),
    path('withdraw', withdraw, name='withdraw'),
    path('signup', signup, name='signup'),
    path('login',signin, name='login'),
    path('logout/', Logout , name='logout'),
    path('claim', claim , name='claim'),

]