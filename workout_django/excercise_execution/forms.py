# forms.py
from django import forms

# class ExerciseExecuteForm(forms.Form):
#     reps = forms.IntegerField(label='Повторения')
#     exercise_title = forms.CharField(label="", max_length=100)
#     def __init__(self, *args, **kwargs):
#         exercise_title = kwargs.pop("exercise_title", {})
#         super().__init__(*args, **kwargs)
#         self.fields["exercise_title"].initial = kwargs.pop("exercise_title", {})
#         if exercise_title is not None:
#             self.fields["exercise_title"].label = exercise_title


class ExerciseExecuteForm(forms.Form):
    exercise_title = forms.CharField(
        widget=forms.HiddenInput(attrs={
            'class': 'exercise-title-display',
            'readonly': 'readonly',
            'style': 'border: none; background: none; font-size: 18px; font-weight: bold; text-align: center;'
            }),
        label='',
        # required=True
    )
    
    reps = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'rep-radio'}),
        label='Количество повторений',
        required=True
    )

    def __init__(self, *args, rep_choices=None, exercise_title='Отжимания', **kwargs):
        super().__init__(*args, **kwargs)
        
        # Устанавливаем динамические choices для повторений
        if rep_choices is not None:
            self.fields['reps'].choices = [(num, str(num)) for num in rep_choices]
        else:
            # Значение по умолчанию (1-30)
            self.fields['reps'].choices = [(i, str(i)) for i in range(1, 31)]
        
        # Устанавливаем начальное значение для exercise_title
        self.fields['exercise_title'].initial = exercise_title