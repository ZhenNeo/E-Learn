from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('enrolled-courses/', views.enrolled_courses, name='enrolled_courses'),
    path('course/<int:course_id>/question-papers/', views.question_papers, name='question_papers'),
    path('course/<int:course_id>/question-papers-modal/', views.question_papers_modal, name='question_papers_modal'),
]
