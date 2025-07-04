
import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from Exercise import Exercise
from Exercise.ExerciseExecution import ExerciseExecutionByTask
from Exercise import Task
from .WorkHttp import RepsWorkDict, WorkHttpGet, WorkHttpPost, WorkJson


class TaskExecutionHttpPost ():
    _taskExecutionHttpGet: 'TaskExecutionHttpGet'
    _workHttpPost: WorkHttpPost
    def __init__(self, 
                 taskExecutionHttpGet: 'TaskExecutionHttpGet',
                 workHttpPost: WorkHttpPost):
        self._taskExecutionHttpGet = taskExecutionHttpGet
        self._workHttpPost = workHttpPost
        
    task = Task(Exercise('Отжимания'), 12, 3)
    task_execution = ExerciseExecutionByTask (task)
    
    def execute(self, request):
        if request.method == 'GET':
            return self._taskExecutionHttpGet.execute(request)
            
        if request.method == 'POST':
            work = WorkJson(
                self._workHttpPost.work_exercise(request)) \
                .work()
            self.task_execution.executeWork(work)
            if self.task_execution.remaind() > 0:
                return HttpResponseRedirect ('/excercise_execute/task-execution/')
            else:
                return HttpResponse(f'Задание выполнено {self.task_execution.as_json()}')
        
        
class TaskExecutionHttpGet ():
    task : Task
    task_execution : ExerciseExecutionByTask
    _workHttpGet : WorkHttpGet
    work_http_post : WorkHttpPost
    def __init__(self, workHttpGet: WorkHttpGet):
        self.task = Task(Exercise('Отжимания'), 12, 3)
        self.task_execution = ExerciseExecutionByTask (self.task)
        self._workHttpGet = workHttpGet
    
    def execute(self, request):
        if request.method == 'GET':
            response = self._workHttpGet.work_exercise(
                request, 
                exercise = self.task._exercise._title,
                remaind_work = self.task._reps,
                task_execution= self.task_execution)
            return response
           
        if request.method == 'POST':
            return TaskExecutionHttpPost().execute(request)