from Exercise import Exercise


class ExerciseStep:
    _exercise: str
    _reps: int
    def __init__(self, exercise: Exercise, reps):
        self._exercise = exercise
        self._reps = reps
    def reps(self):
        return self._reps
    def to_dict(self):
        return {
            'exercise': self._exercise.to_dict(),
            'reps': self._reps
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            Exercise.from_dict(data['exercise']),
            data['reps']
        )