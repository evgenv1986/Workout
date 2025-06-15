# forms.py
from django import forms

class ExerciseExecuteForm(forms.Form):
    reps = forms.IntegerField(label='Повторения')
    
