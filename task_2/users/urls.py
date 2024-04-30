from django.contrib.auth.views import (
    LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView
)
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
      'logout/',
      LogoutView.as_view(template_name='users/logged_out.html'),
      name='logout'
    ),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(template_name='users/password_change_form.html'),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name='password_change_done'
    ),
    path('change_status/<str:username>/', views.change_status, name='change_status'),
    path('update/<str:username>/', views.user_update, name='user_update'),
]
