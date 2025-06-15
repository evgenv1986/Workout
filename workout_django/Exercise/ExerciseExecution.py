from app.workout_django.Exercise import Exercise
from app.workout_django.Exercise.ExerciseTask import ExerciseTask
from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep
from app.workout_django.Exercise.Step.ExerciseSteps import ExerciseSteps


class ExerciseExecution:
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