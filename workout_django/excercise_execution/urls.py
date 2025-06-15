from django.urls import path
from . import views

app_name = 'excercise_execution'

urlpatterns = [
    path('', views.exercise_execute, name='input_exercise_reps'),
]