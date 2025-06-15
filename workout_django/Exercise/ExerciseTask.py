from Exercise import Exercise


class ExerciseTask:
    _exercise: Exercise
    _reps: int
    def __init__(self, exercise: Exercise, reps: int): 
        self._exercise = exercise
        self._reps = reps
    def reps(self):
        return self._reps