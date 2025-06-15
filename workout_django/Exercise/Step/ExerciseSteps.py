from app.workout_django.Exercise.Step.ExerciseStep import ExerciseStep


class ExerciseSteps:
    _steps: list
    def __init__(self):
        self._steps = []
    def add(self, exerciseStep: ExerciseStep):
        self._steps.append (exerciseStep)
        pass
    def reps(self):
        sum: int = 0
        for step in self._steps:
            sum +=  step.reps()
        return sum