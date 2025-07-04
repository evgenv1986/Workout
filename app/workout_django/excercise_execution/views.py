from http.server import BaseHTTPRequestHandler, HTTPServer
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
import json
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy

from Exercise.Step.ExerciseStep import ExerciseStep
from Exercise.Exercise import Exercise
from Exercise.ExerciseExecution import ExerciseExecutionByTask
from Exercise.Task import Task
from excercise_execution.Work import RepsWork
from excercise_execution.Work import Work, TextualWork

from .forms import ExerciseExecuteForm


class ExerciseExecuteView(FormView):
    template_name = 'execution/workout/exercise/excercise2.html'
    form_class = ExerciseExecuteForm
    # success_url = reverse_lazy('exercise_success')
    # default_exercise_title = 'Отжимания'  # Значение по умолчанию

    def post(self, request, *args, **kwargs):
        print("Raw POST data:", request.POST)  # Что действительно пришло с формы
        form = self.get_form()
        if form.is_valid():
            print("Valid form data:", form.cleaned_data)
            return self.form_valid(form)
        else:
            print("Form errors:", form.errors)
            return self.form_invalid(form)

    def get_success_url(self):
        """Динамически генерируем URL для перенаправления"""
        return HttpResponse (
            f'Вы вполнили '
        )
        exercise_title = self.request.session.get('exercise_title', 'Отжимания')
        return reverse('/', kwargs={'exercise_title': exercise_title})
    
    def get_initial(self):
        """Получаем начальное значение для exercise_title из GET-параметра"""
        initial = super().get_initial()
        initial['exercise_title'] = self.get_exercise_title()
        return initial

    def get_exercise_title(self):
         # 1. Проверяем kwargs (переданные в as_view())
        if hasattr(self, 'kwargs') and 'exercise_title' in self.kwargs:
            return self.kwargs['exercise_title']
        # 2. Проверяем GET-параметры
        return self.request.GET.get('exercise_title', self.default_exercise_title)
        # """Получаем exercise_title из GET-параметра или используем значение по умолчанию"""
        # return self.request.GET.get('exercise_title', self.default_exercise_title)

    def get_form_kwargs(self):
        """Передаем параметры в форму"""
        kwargs = super().get_form_kwargs()
        kwargs['exercise_title'] = self.get_exercise_title()
        kwargs['rep_choices'] = self.get_rep_numbers()
        return kwargs

    def get_rep_numbers(self):
        """Метод для получения массива чисел для повторений"""
        # Здесь может быть ваша логика
        return list(range(5, 16))  # Пример: числа от 5 до 15
        
    def form_valid(self, form):
        """Обработка валидной формы"""
        print("POST data:", self.request.POST)  # Отладка
        print("Form data:", form.cleaned_data)  # Отладка
        
        title = form.cleaned_data['exercise_title']
        title = form.cleaned_data.get('exercise_title')
        reps = form.cleaned_data['reps']
        
        self.request.session['exercise_title'] = title
        self.request.session['reps'] = reps
        
        exerciseExecution = ExerciseExecutionByTask(
            Task(Exercise(title), 25))
        exerciseExecution.execute(ExerciseStep(Exercise(title), reps))
        
        self.request.session['remaining'] = exerciseExecution.remaind()
        
        return HttpResponse (
            f'Вы вполнили {title}, количество повторений = {reps} повторений Осталось выполнить {exerciseExecution.remaind()}'
        )
        # return super().form_valid(form)

def add_step(request):
    if request.method == 'GET':
        return render (
            request,
            'execution/workout/exercise/step/step.html')
        
    if request.method == 'POST':
        # title = request.POST.get('exercise_title')
        # request.session['exercise_title'] = title
        
        
        
        reps = request.POST.get('reps')
        if request.session.get('exercise_execution') is None:
            request.session['exercise_execution'] = [
                ExerciseStep(
                    Exercise('pullups'), 
                    reps)
                .to_dict()
            ]
        
        # нужен тест класс и реальный класс, и метод тестирования добавления в сессию, что бы добавлять шаг
        # step_in_session = ExerciseStepInSession(
        #     request.session, 
        #     ExerciseStep(
        #         Exercise('pullups'), 
        #         reps))
        
        request.session['reps'] = reps
        return render (request,
            'execution/workout/exercise/step/step.html', 
            {'completed': request.POST.get('reps')})
    

def exercise_execute(request):        
    if request.method == 'GET':
        exercise_title = "Отжимания"
        # form = ExerciseExecuteForm (initial={'exercise_title': 'Отжимания'})
        return render (
            request,
            'execution/workout/exercise/excercise2.html',
            # {'form': form},
            {'exercise_title' : "Отжимания"}
    )
        
    if request.method == 'POST':
        # form = ExerciseExecuteForm(request.POST)
        # if form.is_valid():
            # request.session['reps'] = form.cleaned_data['reps']
            # reps = request.session['exercise_reps']
            # title = form.cleaned_data['exercise_title']
            # request.session['exercise_title'] = title
            
        
        title = request.POST.get('exercise_title')
        request.session['exercise_title'] = title
        reps = request.POST.get('reps')
        request.session['reps'] = reps
        
        step : ExerciseStep = ExerciseStep (title, reps)
        
        exerciseExecution = ExerciseExecutionByTask (
                Task(
                    Exercise(title),
                    25))
        exerciseExecution.execute(ExerciseStep(Exercise(title), reps))
        # assert 20 == exerciseExecution.remaind()
        
        # if not reps:
            # return HttpResponse("Пожалуйста, выберите количество повторений")
    
        return HttpResponse (
            f'Вы вполнили = {reps} повторений Осталось выполнить {exerciseExecution.remaind()}'
        )
    
     

class TaskExecutable(ABC):
    @abstractmethod
    def execute(self): pass


class WorkRequestDict():
    def __init__(self, request):
        self._request = request
    def work(self):
        return RepsWork (
            self._request.POST.dict()['exercise'],
            self._request.POST.dict()['reps']
        )
   
class TaskExecution(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html_content = """
        <!DOCTYPE html>
        <html>
        <head><title>My Page</title></head>
        <body>
            <h1>Hello from HTTP.Server!</h1>
            <p>You requested: {}</p>
        </body>
        </html>
        """.format(self.path)
        
        self.wfile.write(html_content.encode('utf-8'))
        
    def run():
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, TaskExecution)
        print("Server running on port 8000...")
        httpd.serve_forever()

    if __name__ == "__main__":
        run()