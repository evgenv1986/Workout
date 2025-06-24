import pytest

from Exercise.Exercise import Exercise
from Exercise.ExerciseTask import ExerciseTask
from Exercise.Step.ExerciseStep import ExerciseStep



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
