from django.contrib import admin
from django.urls import path, include
from account.views import user_login

urlpatterns = [
    path("login/", user_login),
]
