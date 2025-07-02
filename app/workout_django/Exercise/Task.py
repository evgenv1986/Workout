from Exercise import Exercise


class Task:
    _exercise: Exercise
    _reps: int
    _lap: int
    
    @classmethod
    def create_with_one_lap(cls, exercise: Exercise, reps: int):
        return Task(exercise, reps, 1)

    def __init__(self, exercise: Exercise, reps: int, lap: int): 
        self._exercise = exercise
        self._reps = reps
        self._lap = lap
    def reps(self):
        return self._reps