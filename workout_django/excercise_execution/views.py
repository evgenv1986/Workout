from django.http import HttpResponse
from django.shortcuts import render

from Exercise.Step.ExerciseStep import ExerciseStep
from Exercise.Exercise import Exercise
from Exercise.ExerciseExecution import ExerciseExecution
from Exercise.ExerciseTask import ExerciseTask

from .forms import ExerciseExecuteForm

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
        
        exerciseExecution = ExerciseExecution (
                ExerciseTask(
                    Exercise(title),
                    25))
        exerciseExecution.execute(ExerciseStep(Exercise(title), reps))
        # assert 20 == exerciseExecution.remaind()
        
        # if not reps:
            # return HttpResponse("Пожалуйста, выберите количество повторений")
    
        return HttpResponse (
            f'Вы вполнили = {reps} повторений Осталось выполнить {exerciseExecution.remaind()}'
        )
    