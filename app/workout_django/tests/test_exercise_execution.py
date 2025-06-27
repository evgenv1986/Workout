import pytest

from Exercise.Exercise import Exercise
from Exercise.ExerciseExecution import ExerciseExecutionByTask
from Workout.app.workout_django.Exercise.Task import Task
from Exercise.Step.ExerciseStep import ExerciseStep

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
            Task(
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
                Task(
                    Exercise('Отжимания'),
                    25)) \
                    .remaind()
    def  test_remaind_after_execution_step(self):
        exerciseExecution = ExerciseExecutionByTask (
                Task(
                    Exercise('Отжимания'),
                    25))
        exerciseExecution.execute(ExerciseStep(Exercise('Отжимания'), 5))
        assert 20 == exerciseExecution.remaind()