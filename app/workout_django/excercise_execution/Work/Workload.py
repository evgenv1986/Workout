
from abc import ABC, abstractmethod


class WorkloadType(ABC):
    @abstractmethod
    def title()-> str: pass
    
class RepsWorkload(WorkloadType):
    _reps: int
    def __init__(self, reps: int):
        self._reps = reps
    def title()-> str: "Повторения"

class TimeWorkload(WorkloadType):
    _minutes: int
    def __init__(self, minutes: int):
        self._minutes = minutes
    def title()-> str: 
        return "Минут"
