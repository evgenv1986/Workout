import pytest

from app.workout_django.Exercise.Exercise import Exercise
from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep



class TestExercise:
    def test_exercise(self):
        exercise = Exercise ('Отжимания')
