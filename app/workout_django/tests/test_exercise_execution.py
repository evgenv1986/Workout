import os
from django.conf import settings
from django.test import TestCase
os.environ['DJANGO_SETTINGS_MODULE'] = 'workout_django.settings' 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workout_django.settings')


from django.test import Client
import pytest
import requests

from Exercise.Exercise import Exercise
from Exercise.ExerciseExecution import ExerciseExecutionByTask, TaskExecution, TaskExecutionInputDataForm
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
        
    def test_begin_execution(self):
        texec = TaskExecution()
        assert 1==1
        
    
class TestHttpTestWork(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        if not settings.configured:
            settings.configure()
    
    def test_task_execution_input_form(self):
        inputForm = TaskExecutionInputDataForm(
            client = Client(),
            url = '/excercise_execute/work/',
            task_execution = ExerciseExecutionByTask (Task(Exercise('Отжимания'), 125, 3))
        )
        
        inputForm.execute()
    