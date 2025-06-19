import pytest

from app.workout_django.Exercise.Exercise import Exercise
from app.workout_django.Exercise.ExerciseExecution import ExerciseExecutionByTask
from app.workout_django.Exercise.ExerciseTask import ExerciseTask
from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep

class ExerciseExecution:
    def execute(self, exerciseStep: ExerciseStep, reps: int): pass

class TestExerciseExecution:
    def test_exercise_execution_creation(self):
        exercise = ExerciseExecution ()
        exercise.execute (
            ExerciseStep(
                Exercise('pullups'), 25))
        
        
        
    def test_execution(self):
        execution = ExerciseExecutionByTask (
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
            ExerciseExecutionByTask (
                ExerciseTask(
                    Exercise('Отжимания'),
                    25)) \
                    .remaind()
    def  test_remaind_after_execution_step(self):
        exerciseExecution = ExerciseExecutionByTask (
                ExerciseTask(
                    Exercise('Отжимания'),
                    25))
        exerciseExecution.execute(ExerciseStep(Exercise('Отжимания'), 5))
        assert 20 == exerciseExecution.remaind()