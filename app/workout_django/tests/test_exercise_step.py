import pytest

from Exercise.Exercise import Exercise
from Exercise.Step.ExerciseStep import ExerciseStep
from excercise_execution.Work.Workload import WorkloadAbstract, RepsWorkload, MinutesWorkload

class TestExerciseStep:
    def test_exercise_step(self):
        assert 3 == ExerciseStep (Exercise('Отжимания'), 3).reps()

    def test_add_reps_work_to_exercise_step(self):
        reps = RepsWorkload(25)
        assert RepsWorkload(25) == ExerciseStep (Exercise('Отжимания'), reps).work()

    def test_create_step_with_time_workload(self):
        assert 3 == ExerciseStep.create_step_with_workload (
            Exercise('Отжимания'), 
            MinutesWorkload()) \
            .reps()
