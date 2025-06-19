from Exercise import Exercise


class ExerciseTask:
    _exercise: Exercise
    _reps: int
    _lap: int
    def __init__(self, exercise: Exercise, reps: int): 
        self._exercise = exercise
        self._reps = reps
    def __init__(self, exercise: Exercise, reps: int, lap: int): 
        self._exercise = exercise
        self._reps = reps
        self._lap = lap
    def reps(self):
        return self._reps