from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('enrolled-courses/', views.enrolled_courses, name='enrolled_courses'),
    path('course/<int:course_id>/previous_question_papers/', views.previous_question_papers, name='previous_question_papers'),
]
