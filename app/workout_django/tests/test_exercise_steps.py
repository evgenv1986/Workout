import pytest

from Exercise.Step.ExerciseStep import ExerciseStep
from Exercise.Step.ExerciseSteps import ExerciseSteps

class TestExerciseSteps:
    def test_exercise_steps_add(self):
        ExerciseSteps().add ( 
            ExerciseStep('Отжимания', 3))
    def test__exercise_steps_reps(self):
        steps = ExerciseSteps()
        steps.add (ExerciseStep('Отжимания', 3))
        assert 3 == steps.reps()    
        steps.add(ExerciseStep('Отжимания', 2))
        assert 3 + 2 == steps.reps()
        
    def test_steps_count(self):
        steps = ExerciseSteps()
        steps.add (ExerciseStep('Отжимания', 3))
        steps.add (ExerciseStep('Отжимания', 2))
        assert 2 == steps.count()
        