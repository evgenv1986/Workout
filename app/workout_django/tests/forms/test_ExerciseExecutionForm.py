import pytest
from django import forms

from app.workout_django.excercise_execution.forms import ExerciseExecutionForm

@pytest.mark.parametrize("rep_choices,expected_choices", [
    ([5, 10, 15], [(5, '5'), (10, '10'), (15, '15')]),
    (range(1, 4), [(1, '1'), (2, '2'), (3, '3')]),
    (None, [(i, str(i)) for i in range(1, 31)]),  # Проверка значения по умолчанию
])
def test_rep_choices_initialization(rep_choices, expected_choices):
    form = ExerciseExecutionForm(rep_choices=rep_choices)
    assert form.fields['reps'].choices == expected_choices

def test_form_initial_title():
    form = ExerciseExecutionForm(exercise_title='Приседания')
    assert form.fields['exercise_title'].initial == 'Приседания'

def test_form_default_title():
    form = ExerciseExecutionForm()
    assert form.fields['exercise_title'].initial == 'Отжимания'

def test_form_validation():
    form_data = {
        'exercise_title': 'Подтягивания',
        'reps': '10'
    }
    form = ExerciseExecutionForm(data=form_data, rep_choices=[5, 10, 15])
    assert form.is_valid()
    assert form.cleaned_data['exercise_title'] == 'Подтягивания'
    assert form.cleaned_data['reps'] == '10'

def test_invalid_rep_choice():
    form_data = {
        'exercise_title': 'Подтягивания',
        'reps': '20'  # 20 нет в допустимых значениях
    }
    form = ExerciseExecutionForm(data=form_data, rep_choices=[5, 10, 15])
    assert not form.is_valid()