from Exercise import Exercise
from Exercise.ExerciseTask import ExerciseTask
from Exercise.Step.ExerciseStep import ExerciseStep
from Exercise.Step.ExerciseSteps import ExerciseSteps
from excercise_execution.Work import RepsWork
from excercise_execution.Work import Work


class ExerciseExecutionByTask:
    _exerciseTask: ExerciseTask
    _exerciseSteps: ExerciseSteps
    _works = []
    def __init__(self, exerciseTask: ExerciseTask):
        self._exerciseTask = exerciseTask
        self._exerciseSteps = ExerciseSteps()
    def execute(self, exerciseStep: ExerciseStep):
        self._exerciseSteps.add(exerciseStep)
    def executeWork(self, work: RepsWork):
        self._works.append(work)
    def remaind(self): 
        works_reps = 0
        for w in self._works:
            works_reps += int (w.doned_work())
        return (
            self._exerciseTask.reps() - 
            # self._exerciseSteps.reps()
            works_reps
        )
    def as_json(self):
        return {self._exerciseTask._exercise._title: self._exerciseTask._reps}