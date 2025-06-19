from Exercise import Exercise
from Exercise.ExerciseTask import ExerciseTask
from Exercise.Step.ExerciseStep import ExerciseStep
from Exercise.Step.ExerciseSteps import ExerciseSteps


class ExerciseExecutionByTask:
    _exerciseTask: ExerciseTask
    _exerciseSteps: ExerciseSteps
    def __init__(self, exerciseTask: ExerciseTask):
        self._exerciseTask = exerciseTask
        self._exerciseSteps = ExerciseSteps()
    def execute(self, exerciseStep: ExerciseStep):
        self._exerciseSteps.add(exerciseStep)
    def remaind(self): 
        return (
            self._exerciseTask.reps() - 
            self._exerciseSteps.reps())