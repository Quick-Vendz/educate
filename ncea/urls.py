# ncea urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('rubric-creator/', views.rubric_creator, name='ncea-rubric-creator'),
]