from django.http import HttpResponse
from django.shortcuts import render

def input_exercise_reps(request):        
    if request.method == 'POST':
        reps_completed = request.POST.get('reps')
        
    
    return render (
        request,
        'execution/workout/exercise/excercise2.html',
    )
    