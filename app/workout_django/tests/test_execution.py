import pytest

from Exercise import Exercise
from Exercise.ExerciseExecution import ExerciseExecutionByTask
from Exercise.Task import Task
from excercise_execution.Work.Workload import RepsWorkloadType, Workload

class TestExerciseExecution:
    def test_execution_from_start_to_finish(self):
        work = Workload(Exercise('pullups'), 25, RepsWorkloadType())
        task_execution = ExerciseExecutionByTask (
                Task(Exercise('Отжимания'), 25, 3))
        task_execution.executeWork(work)
        # work.add(work)

