from django.contrib import admin
from django.urls import path, include

from students.views import all_students, student, create_student, edit_student

app_name = "students"

urlpatterns = [
    path('allStudents/', all_students, name='all_students'),
    path('student/<int:pk>/', student, name='student'),
    path('createStudent', create_student, name='create_student'),
    path('editStudent/<int:pk>/', edit_student, name='edit_student'),
]
