from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', index, name='index'),
    path('withdraw', withdraw, name='withdraw'),
    path('signup', signup, name='signup'),
    path('login',signin, name='login'),
    path('logout/', Logout , name='logout'),
    path('claim', claim , name='claim'),
    path('<int:id>/click/', claimid, name='claimid'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset.html',
            success_url = '/reset_password_sent'),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='email.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='reset.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='finish.html'),name="password_reset_complete"),

]