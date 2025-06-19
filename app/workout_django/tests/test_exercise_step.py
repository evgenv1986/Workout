import pytest

from app.workout_django.Exercise.Exercise import Exercise
from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep

class TestExerciseStep:
    def test_exercise_step(self):
        assert 3 == ExerciseStep (Exercise('Отжимания'), 3).reps()
