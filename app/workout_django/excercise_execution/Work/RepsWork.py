from abc import ABC
from excercise_execution.Work.Workload import WorkloadAbstract
from excercise_execution.Work.Work import TextualWork, Work


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
    def exercise(self)-> str: 
        return self.json.loads(self._response.content)['exercise']
    def workload_type(self)-> WorkloadAbstract: pass
        # return self.json.loads(self._response.content)['reps'] здесь нужно type а не количество повторений вернуть, 
    def execute(self):
        pass
    
    
class WorkImp (Work):
    def __init__(
        self,
        workload_type: WorkloadAbstract,
        amount: int):
        pass
    def execute(self):
        pass
    def workload_type(self)-> str: 
        pass