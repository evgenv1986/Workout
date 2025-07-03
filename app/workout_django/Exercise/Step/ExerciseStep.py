from Exercise import Exercise
from excercise_execution.Work import Workload


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
    def create_step_with_workload (cls, exercise: Exercise, work_type: Workload.WorkloadType):
        pass
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            Exercise.from_dict(data['exercise']),
            data['reps']
        )