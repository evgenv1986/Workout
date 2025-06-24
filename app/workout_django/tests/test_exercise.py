import pytest

from Exercise.Exercise import Exercise
from Exercise.Step.ExerciseStep import ExerciseStep



class TestExercise:
    def test_exercise(self):
        exercise = Exercise ('Отжимания')
        assert Exercise ('Отжимания').__eq__(exercise)