from django.urls import path
from django.utils.encoding import escape_uri_path
import requests

from .views import ExerciseExecuteView, HttpWork, TaskExecutionHttp, exercise_execute, add_step

# from app.workout_django.excercise_execution import views
# from excercise_execution.views import views

app_name = 'excercise_execution'

work = HttpWork()
taskExecutionHttp = TaskExecutionHttp()
urlpatterns = [
    # path('', exercise_execute, name='input_exercise_reps'),
    # path('<str:exercise_title>/', ExerciseExecuteView.as_view(), name='exercise-custom'),
    path('add_step/', add_step, name='add_step'),
    path('work/', work.work, name='work'),
    path('task-execution/', taskExecutionHttp.execute, name='task-execution'),
]