from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:roll_number>/', views.student_profile, name='student_profile'),
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('feedback/', views.feedback_form, name='feedback_form'),
]
