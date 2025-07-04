
from abc import ABC, abstractmethod


class Workload(ABC):
    @abstractmethod
    def title()-> str: 
        pass
    @abstractmethod
    def as_string()-> str: 
        pass
    
class RepsWorkload(Workload):
    _reps: int
    def __init__(self, reps: int):
        self._reps = reps
    def title(self)-> str: 
        return "повторени(я/й/е)"
    def as_string(self)-> str: 
        return f'{self._reps} {self.title()}'
    

class TimeWorkload(Workload):
    _minutes: int
    def __init__(self, minutes: int):
        self._minutes = minutes
    def title(self)-> str: 
        return "минут(а/ы)"
    def as_string(self)-> str: 
        return f'{self._minutes} {self.title()}'
