import pytest

from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep

class TestExerciseStep:
    def test_exercise_step(self):
        assert 3 == ExerciseStep ('Отжимания', 3).reps()
