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
    def test_task_reps(self):
        assert 25 == ExerciseTask (
            Exercise('Отжимания'),
            25) \
            .reps()
    def test_lap(self):
        assert 2 == ExerciseTask(
            exercise = Exercise('Отжимания'), 
            reps = 25,
            lap = 2   
        )
