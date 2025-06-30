from django.urls import path
from django.utils.encoding import escape_uri_path
import requests

from Exercise import TaskExecutionInputDataForm, ExerciseExecutionByTask, Task, Exercise


from .views import ExerciseExecuteView, TaskExecutionHttpPost, WorkHttpGet, TaskExecutionHttpGet, WorkHttpPost, exercise_execute, add_step

# from app.workout_django.excercise_execution import views
# from excercise_execution.views import views

app_name = 'excercise_execution'

work = WorkHttpGet()
taskExecutionHttp = TaskExecutionHttpGet()

# такая схема: дописать параметры в конструкторы классов
taskExecution = TaskExecutionHttpPost(
                    TaskExecutionHttpGet(
                        WorkHttpGet()
                    ),
                    WorkHttpPost()
)

# TaskExecutionHttpPost.get -> TaskExecutionHttpGet.get -> WorkHttpGet.get(render form)
# TaskExecutionHttpPost.post -> WorkHttpPost.post() -> json -> TaskExecutionHttpPost.post
# TaskExecutionHttpPost.post -> response taskExecution object

# TODO: 
# Добавить вызов Workout:
# Workout - task execution - work - task execution - workout - end

urlpatterns = [
    # path('', exercise_execute, name='input_exercise_reps'),
    # path('<str:exercise_title>/', ExerciseExecuteView.as_view(), name='exercise-custom'),
    path('add_step/', add_step, name='add_step'),
    path('work/', work.work, name='work'),
    path('work_exercise/<str:exercise>/', work.work_exercise, name='work_exercise'),
    path('task-execution/', taskExecutionHttp.execute, name='task-execution'),
    # path('task-execution/begin', taskExecutionHttp.show_form_executing_work, name='task-execution'),
    path('TaskExecutionInputDataForm/', 
         TaskExecutionInputDataForm(
            task_execution = ExerciseExecutionByTask (Task(Exercise('Отжимания'), 125, 3)))
         .execute, name='execute'),
    

    # path # "workout/execute/create -> get:Html -> post: Json-Workout",
    # path ("""workout/execute/
    #                     tasks=[
    #                         {pullups, workload=25, laps=3},
    #                         {pushups, workload=15, laps=4},
    #                     ]
    #         """
    #     ),
]