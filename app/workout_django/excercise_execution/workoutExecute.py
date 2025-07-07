from django.shortcuts import render
from .workoutExecuteViewModel import WorkoutForm

def workout_execute(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            # ...
            return render(request, 'success.html')
    else:
        form = WorkoutForm()
    
    return render(request, 'workoutExecuteView.html', 
                  {'form': form})