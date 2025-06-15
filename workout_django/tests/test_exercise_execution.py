import pytest

from app.workout_django.Exercise.Exercise import Exercise
from app.workout_django.Exercise.ExerciseExecution import ExerciseExecution
from app.workout_django.Exercise.ExerciseTask import ExerciseTask
from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep



class TestExerciseExecution:
    def test_exercise_execution_creation(self):
        execution = ExerciseExecution (
            ExerciseTask(
                Exercise('Отжимания'),
                25),
        )
    def test_execution(self):
        execution = ExerciseExecution (
            ExerciseTask(
                Exercise('Отжимания'),
                25))
        execution.execute(
            ExerciseStep (
                Exercise('Отжимания'), 
                3)
        )
    def test_remaind(self):
        assert 25 == \
            ExerciseExecution (
            ExerciseTask(
                Exercise('Отжимания'),
                25)) \
                .remaind()