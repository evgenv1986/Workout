from django.urls import path
from django.utils.encoding import escape_uri_path

from .views import ExerciseExecuteView, exercise_execute, exercise_step

# from app.workout_django.excercise_execution import views
# from excercise_execution.views import views

app_name = 'excercise_execution'

urlpatterns = [
    # path('', exercise_execute, name='input_exercise_reps'),
    path('<str:exercise_title>/', ExerciseExecuteView.as_view(), name='exercise-custom'),
    path('exercise_step/', exercise_step, name='exercise_step'),
]