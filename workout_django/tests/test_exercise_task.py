import pytest

from app.workout_django.Exercise.Exercise import Exercise
from app.workout_django.Exercise.ExerciseTask import ExerciseTask
from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep



class TestExerciseTask:
    def test_exercise_task(self):
        task = ExerciseTask (
            Exercise('Отжимания'),
            25
        )


