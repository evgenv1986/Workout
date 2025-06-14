from django.http import HttpResponse
from django.shortcuts import render

def input_exercise_reps(request):        
    if request.method == 'POST':
        reps = request.POST.get('reps')
        if not reps:
            return HttpResponse("Пожалуйста, выберите количество повторений")
    
    return render (
        request,
        'execution/workout/exercise/excercise2.html',
    )
    