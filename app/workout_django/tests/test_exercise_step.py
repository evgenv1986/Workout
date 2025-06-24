import pytest

from Exercise.Exercise import Exercise
from Exercise.Step.ExerciseStep import ExerciseStep

class TestExerciseStep:
    def test_exercise_step(self):
        assert 3 == ExerciseStep (Exercise('Отжимания'), 3).reps()
