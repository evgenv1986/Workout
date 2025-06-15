# forms.py
from django import forms

class ExerciseExecuteForm(forms.Form):
    reps = forms.IntegerField(label='Повторения')
    exercise_title = forms.CharField(label="", max_length=100)
    def __init__(self, *args, **kwargs):
        exercise_title = kwargs.pop("exercise_title", {})
        super().__init__(*args, **kwargs)
        self.fields["exercise_title"].initial = kwargs.pop("exercise_title", {})
        if exercise_title is not None:
            self.fields["exercise_title"].label = exercise_title
