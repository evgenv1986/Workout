from app.workout_django.Exercise import Exercise
from app.workout_django.Exercise.ExerciseTask import ExerciseTask
from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep


class ExerciseExecution:
    def __init__(self,
                 exerciseTask: ExerciseTask):pass
    def execute(self, exerciseStep: ExerciseStep):pass
    def remaind(self): 
        return self._exerciseTask.reps() - self._exerciseSteps.sumReps()