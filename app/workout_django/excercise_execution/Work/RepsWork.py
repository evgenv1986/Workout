from abc import ABC
from excercise_execution.Work.Work import TextualWork


class RepsWork(TextualWork):
    _exercise: str
    _reps: int
    def __init__(self, exercise: str, reps: int):
        self._exercise = exercise
        self._reps = reps
    def work (self): 
        return self._reps
    def as_dict(self):
        return {'exercise': self._exercise, 'reps': self._reps}
    def as_string(self) -> str: 
        return f'{self._exercise} {self._reps} repetitions'
    
