from excercise_execution.Work.Work import TextualWork


class RepsWork(TextualWork):
    _exercise: str
    _reps: int
    def __init__(self, exercise: str, reps: int):
        self._exercise = exercise
        self._reps = reps
    def doned_work (self): pass
    def as_json(self):
        return {'exercise': self._exercise, 'reps': self._reps}
    def as_string(self) -> str: 
        return self._exercise
    
