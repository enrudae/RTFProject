from django.contrib import admin
from django.urls import path, include

from students.views import profile_view, RegisterView

app_name = "students"

urlpatterns = [
    path('profile', profile_view, name='profile'),
    path('register', RegisterView.as_view(), name='register'),
]
