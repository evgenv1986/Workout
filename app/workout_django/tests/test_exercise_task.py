import pytest

from Exercise.Exercise import Exercise
from Workout.app.workout_django.Exercise.Task import Task
from Exercise.Step.ExerciseStep import ExerciseStep



class TestExerciseTask:
    def test_exercise_task(self):
        task = Task (
            Exercise('Отжимания'),
            25
        )
    def test_task_reps(self):
        assert 25 == Task (
                        Exercise('Отжимания'),
                        25) \
                        .reps()
    def test_lap(self):
        assert 2 == Task(
            exercise = Exercise('Отжимания'), 
            reps = 25,
            lap = 2   
        )
