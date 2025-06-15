from app.workout_django.Exercise import Exercise


class ExerciseStep:
    _exercise: str
    _reps: int
    def __init__(self, exercise: Exercise, reps):
        self._exercise = exercise
        self._reps = reps
    def reps(self):
        return self._reps