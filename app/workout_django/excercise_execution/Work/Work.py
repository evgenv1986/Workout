
from abc import ABC, abstractmethod
from .Workload import WorkloadType

class Work(ABC):
    @abstractmethod
    def work (self)-> 'Work': pass
    @abstractmethod
    def exercise(self)-> str: pass
    @abstractmethod
    def workload(self)-> WorkloadType: pass
    
class Textual(ABC):
    @abstractmethod
    def as_dict(self) -> str: pass 
    @abstractmethod
    def as_string(self) -> str: pass 
    


class TextualWork(Work, Textual):
    @abstractmethod
    def work (self)-> 'Work': pass
    @abstractmethod
    def as_dict(self) -> str: pass
    @abstractmethod
    def as_string(self) -> str: pass
    @abstractmethod
    def exercise(self)-> str: pass
    @abstractmethod
    def workload(self)-> WorkloadType: pass
   
   