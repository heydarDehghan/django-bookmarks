from django.contrib import admin
from django.urls import path, include
from account.views import user_login, dashboard
from django.contrib.auth import views as auth_view

urlpatterns = [
    # path("login/", user_login),
    path("login/", auth_view.LoginView.as_view(), name='login'),
    path("logout/", auth_view.LogoutView.as_view(), name='logout'),
    path("", dashboard, name='dashboard')
]
