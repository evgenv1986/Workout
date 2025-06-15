from django.http import HttpResponse
from django.shortcuts import render

from .forms import ExerciseExecuteForm

class ExerciseStep:
    title: str
    reps: int
    def __init__(self, title, reps):
        self.title = title
        self.reps = reps

def exercise_execute(request):        
    if request.method == 'GET':
        form = ExerciseExecuteForm ()
        return render (
            request,
            'execution/workout/exercise/excercise2.html',
            {'form': form}
    )
        
    if request.method == 'POST':
        form = ExerciseExecuteForm(request.POST)
        if form.is_valid():
            request.session['reps'] = form.cleaned_data['reps']
            reps = request.session['reps']
        
        title = request.POST.get('exercise_title')
        reps = request.POST.get('exercise_reps')
        if not reps:
            return HttpResponse("Пожалуйста, выберите количество повторений")
    
    step : ExerciseStep = ExerciseStep (title, reps)
    
    return render (
        request,
        'execution/workout/exercise/excercise2.html',
    )
    