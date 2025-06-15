import pytest

from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep
from app.workout_django.Exercise.Step.ExerciseSteps import ExerciseSteps

class TestExerciseSteps:
    def test_exercise_steps_add(self):
        ExerciseSteps().add ( 
            ExerciseStep('Отжимания', 3).reps())
