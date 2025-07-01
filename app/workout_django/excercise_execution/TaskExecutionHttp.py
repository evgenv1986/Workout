
import json

from django.http import HttpResponse, JsonResponse
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
        
    task = Task(Exercise('Отжимания'), 125, 3)
    task_execution = ExerciseExecutionByTask (task)
    
    def execute(self, request):
        if request.method == 'GET':
            return self._taskExecutionHttpGet.execute(request)
            
        if request.method == 'POST':
            response = self._workHttpPost.work_exercise(request)
            work = WorkJson(
                self._workHttpPost.work_exercise(request)) \
                .work()
            self.task_execution.executeWork(work)
            return HttpResponse(self.task_execution)
        
        
class TaskExecutionHttpGet ():
    task : Task
    task_execution : ExerciseExecutionByTask
    _workHttpGet : WorkHttpGet
    work_http_post : WorkHttpPost
    def __init__(self, workHttpGet: WorkHttpGet):
        self.task = Task(Exercise('Отжимания'), 125, 3)
        self.task_execution = ExerciseExecutionByTask (self.task)
        self._workHttpGet = workHttpGet
    
    def execute(self, request):
        if request.method == 'GET':
            # self._workHttpGet = WorkHttpGet (WorkHttpPost(), exercise = self.task._exercise)
            response = self._workHttpGet.work_exercise(request, exercise = self.task._exercise._title)
            return response
            # data = request.POST.dict()
            
            # data = request.POST.dict()
            # # if not len(data.items()) == 0:
            # cache_key = f"temp_data_{request.user.id}"
            # work = cache.get(cache_key)
            # remaind = self.task_execution.remaind()
            # task_work = self.task_execution.task_work()
            
            #     # work = WorkRequestDict(request).work()
            # return render(request,
            #               'execution/workout/taskExecution/taskExecution.html',
            #               {'task_execution': self.task_execution,
            #                'work_execute': "execution/workout/exercise/step/step.html"
            #                })
            
            # if self.taskExecution.remaind() > 0:
            # return HttpResponse(HttpWork().work(request))
       
        if request.method == 'POST':
            return TaskExecutionHttpPost().execute(request)
            
            # self.work_http_post = WorkHttpPost()
            # work_response = self.work_http_post.work_exercise(request)
            # content_type = request.headers.get('Content-Type', '')
            # if 'application/json' in content_type:
            #     try:
            #         if not request.body:
            #             return JsonResponse({'error': 'Empty request body'}, status=400)
            #         data = json.loads(request.body)
            #     except json.JSONDecodeError:
            #         return JsonResponse({'error': 'Invalid JSON format'}, status=400)
            # else:
            #     # Для form-data/x-www-form-urlencoded
            #     data = request.POST.dict()
            # # data = request.POST.dict()  
            # exercise = data['exercise']
            # reps = data['reps']
            # work = WorkRequestDict(request).work() 
            # # work = HttpWork().work(request)
            
            # self.task_execution.executeWork(work)
            # remaind = self.task_execution.remaind()
            
            # cache_key = f"temp_data_{request.user.id}"
            # cache.set(cache_key, work, timeout=300)  # 5 минут
            
            # # if not task.completed: повторить ввод выполнения упражнения
            # return HttpResponse(self.task_execution)
            
            # return HttpResponseRedirect ('/excercise_execute/task-execution/')
            # else:
                # return подумать куда перейти

            # return HttpResponseRedirect('/excercise_execute/work/')
       
     