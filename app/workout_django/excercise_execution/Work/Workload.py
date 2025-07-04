
from abc import ABC, abstractmethod


class Workload(ABC):
    @abstractmethod
    def title()-> str: 
        pass
    @abstractmethod
    def as_string()-> str: 
        pass
    @abstractmethod
    def add(self, work: 'Workload'): 
        pass
    @abstractmethod
    def value(self)-> int: 
        pass
    @abstractmethod
    def total_work_value(self)-> int: 
        pass
    @abstractmethod
    def next(self)-> 'Workload': 
        pass
    @abstractmethod
    def set_next_as_empty():
        pass
    
class RepsWorkload(Workload):
    _reps: int
    _next: Workload
    def __init__(self, reps: int):
        self._reps = reps
    def title(self)-> str: 
        return "повторени(я/й/е)"
    def as_string(self)-> str: 
        return f'{self._reps} {self.title()}'
    def add(self, work: Workload): 
        pass
    def value(self)-> int: 
        pass
    def total_work_value(self)-> int: 
        reps_next_work = RepsWorkload(self._next)
        return RepsWorkload (reps_next_work._reps)
        total = 0
        for n in self.next():
            self._reps += n.value()
    # def next(self)-> 'Workload': 
        # pass

class EmptyWorkload(Workload):
    def __init__(self):
        pass
    def title(self)-> str: 
        return "Empty workload"
    def as_string(self)-> str: 
        return ""
    def add(self, work: 'Workload'): 
        pass
    def value(self)-> int: 
        return 0
    def total_work_value(self)-> int: 
        return 0
    def next(self)-> 'Workload': 
        pass
    def set_next_as_empty(self):
        pass
    
    
    
class MinutesWorkload(Workload):
    _minutes: int
    _next: Workload
    def __init__(self, minutes: int):
        self._minutes = minutes
        self.set_next_as_empty()
    def set_next_as_empty(self):
        self._next = EmptyWorkload()
    def title(self)-> str: 
        return "минут(а/ы)"
    def as_string(self)-> str: 
        return f'{self._minutes} {self.title()}'
    def add(self, work: Workload): 
        self._next = MinutesWorkload(work.value())
    def value(self)-> int: 
        return self._minutes
    def total_work_value(self)-> int: 
        total: int = 0
        total += self.value() + self._next.value()
        return total
    def next(self):
        return self._next