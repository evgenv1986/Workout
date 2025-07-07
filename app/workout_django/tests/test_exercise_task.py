import pytest

from Exercise.Exercise import Exercise
from Exercise.Task import Task
from Exercise.Step.ExerciseStep import ExerciseStep



class TestExerciseTask:
    def test_exercise_task(self):
        task = Task.create_with_one_lap (
            Exercise('Отжимания'),
            25,
        )
    def test_task_reps(self):
        assert 25 == Task.create_with_one_lap (
                        Exercise('Отжимания'),
                        25) \
                        .reps()
    def test_lap(self):
        assert 2 == Task(
            exercise = Exercise('Отжимания'), 
            reps = 25,
            lap = 2   
        )._lap
