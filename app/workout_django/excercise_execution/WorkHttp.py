import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from Exercise.ExerciseExecution import ExerciseExecutionByTask

from .Work.Workload import WorkloadType
from .Work import Work, TextualWork
from excercise_execution.Work import RepsWork
from Exercise import Exercise

class WorkJson(Work):
    _response: JsonResponse
    def __init__(self, response: JsonResponse):
        self._response = response
    def work(self)-> Work:
        work_dict = json.loads(self._response.content)
        return RepsWork(
            work_dict['exercise'],
            work_dict['reps']
        )
    def exercise(self)-> str: 
        return self.json.loads(self._response.content)['exercise']
    
    def workload_type(self)-> WorkloadType: pass
        # return self.json.loads(self._response.content)['reps'] здесь нужно type а не количество повторений вернуть, 
    
    
class RepsWorkDict(TextualWork):
    _request: HttpRequest
    def __init__(self, request: HttpRequest):
        self._request = request
    def work(self)-> Work:
        return RepsWork(
            self._request.POST.dict()['exercise'],
            self._request.POST.dict()['reps']
        )
    def as_dict(self) -> str:
        return {'exercise': self._request.POST.dict()['exercise'], 
                'reps': self._request.POST.dict()['reps']}
    def as_string(self) -> str: 
        pass
    def exercise(self)-> str: pass
    def workload_type(self)-> WorkloadType: pass
    
class WorkHttpPost():
    _exercise: Exercise
    def __init(self): pass
        
    def work_exercise (self, request: HttpRequest): 
       if request.method == 'POST':
           work_dict = RepsWorkDict (request)
           dict_ = work_dict.as_dict()
           return JsonResponse(dict_)

    
class WorkHttpGet():
    _work: RepsWork
    _workPost : WorkHttpPost
    _exercise: Exercise
    def __init__(self, workPost: WorkHttpPost, exercise: Exercise):
        self._workPost = workPost
        self._exercise = exercise
    
    def work_exercise (self, 
                       request: HttpRequest, 
                       exercise: str, 
                       remaind_work: int,
                       task_execution: ExerciseExecutionByTask) -> HttpResponse: 
        if request.method == 'GET':
            # return render (
            #     request,
            #     'execution/workout/exercise/step/step.html',
            #     {'exercise': exercise,
            #      'remaind_work': remaind_work,
            #     }
            # )
            return render(
                request,
                'execution/workout/taskExecution/taskExecution.html',
                {'task_execution': task_execution,
                'work_execute': "execution/workout/exercise/step/step.html",
                'exercise': exercise,
                'remaind_work': remaind_work,})
    
    
        if request.method == 'POST':
            data = {}        
            content_type = request.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                try:
                    if not request.body:
                        return JsonResponse({'error': 'Empty request body'}, status=400)
                    data = json.loads(request.body)
                except json.JSONDecodeError:
                    return JsonResponse({'error': 'Invalid JSON format'}, status=400)
            else:
                # Для form-data/x-www-form-urlencoded
                data = request.POST.dict()
            self._work = RepsWork(data.get('exercise'), data.get('reps'))
            return JsonResponse(self._work.as_dict()) # возврат выволненного упражнения ввиде json