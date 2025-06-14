from django.urls import path
from . import views

app_name = 'excercise_execution'

urlpatterns = [
    path('', views.input_exercise_reps, name='input_exercise_reps'),
]