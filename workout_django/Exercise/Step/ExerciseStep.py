class ExerciseStep:
    _title: str
    _reps: int
    def __init__(self, title, reps):
        self._title = title
        self._reps = reps
    def reps(self):
        return self._reps