
from abc import ABC, abstractmethod

from Exercise import Exercise


class WorkloadAbstract(ABC):
    @abstractmethod
    def title()-> str: 
        pass
    @abstractmethod
    def as_string()-> str: 
        pass
    @abstractmethod
    def add(self, work: 'WorkloadAbstract'): 
        pass
    @abstractmethod
    def value(self)-> int: 
        pass
    @abstractmethod
    def total_work_value(self)-> int: 
        pass
    @abstractmethod
    def next(self)-> 'WorkloadAbstract': 
        pass
    @abstractmethod
    def set_next_as_empty():
        pass
    
class RepsWorkload(WorkloadAbstract):
    _reps: int
    _next: WorkloadAbstract
    def __init__(self, reps: int):
        self._reps = reps
    def title(self)-> str: 
        return "повторени(я/й/е)"
    def as_string(self)-> str: 
        return f'{self._reps} {self.title()}'
    def add(self, work: WorkloadAbstract): 
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

class EmptyWorkload(WorkloadAbstract):
    def __init__(self):
        pass
    def title(self)-> str: 
        return "Empty workload"
    def as_string(self)-> str: 
        return ""
    def add(self, work: 'WorkloadAbstract'): 
        pass
    def value(self)-> int: 
        return 0
    def total_work_value(self)-> int: 
        return 0
    def next(self)-> 'WorkloadAbstract': 
        pass
    def set_next_as_empty(self):
        pass
    
    
    
class MinutesWorkload(WorkloadAbstract):
    _minutes: int
    _next: WorkloadAbstract
    def __init__(self, minutes: int):
        self._minutes = minutes
        self.set_next_as_empty()
    def set_next_as_empty(self):
        self._next = EmptyWorkload()
    def title(self)-> str: 
        return "минут(а/ы)"
    def as_string(self)-> str: 
        return f'{self._minutes} {self.title()}'
    def add(self, work: WorkloadAbstract): 
        self._next = MinutesWorkload(work.value())
    def value(self)-> int: 
        return self._minutes
    def total_work_value(self)-> int: 
        total: int = 0
        total += self.value() + self._next.value()
        return total
    def next(self):
        return self._next
    
    
class WorkloadType(ABC):
    @abstractmethod
    def title()-> str: 
        pass     
class MinutesWorkloadType(WorkloadType):
    def title(self)-> str: 
        return "минут(а/ы)"

class RepsWorkloadType(WorkloadType):
    def title(self)-> str: 
        return "Повторение(я)"
    
    
class Workload(WorkloadAbstract):
    _minutes: int
    _next: WorkloadAbstract
    _workload_type: WorkloadType
    _exercise: Exercise
    def __init__(self, 
                 exercise: Exercise,
                 value: int, 
                 workloadType: WorkloadType):
        self._minutes = value
        self._workload_type = workloadType
        self._exercise = exercise
        self.set_next_as_empty()
    def set_next_as_empty(self):
        self._next = EmptyWorkload()
    def title(self)-> str: 
        pass
    def as_string(self)-> str: 
        return f'{self._minutes} {self._workload_type.title()}'
    def add(self, work: WorkloadAbstract): 
        self._next = MinutesWorkload(work.value())
    def value(self)-> int: 
        return self._minutes
    def total_work_value(self)-> int: 
        total: int = 0
        total += self.value() + self._next.value()
        return total
    def next(self):
        return self._next