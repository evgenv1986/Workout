
from abc import ABC, abstractmethod
from .Workload import WorkloadType

class Work(ABC):
    @abstractmethod
    def workload_type(self)-> WorkloadType: 
        pass
    @abstractmethod
    def execute(self): 
        pass
    
class Textual(ABC):
    @abstractmethod
    def as_dict(self) -> str: 
        pass 
    @abstractmethod
    def as_string(self) -> str: 
        pass 
    

class TextualWork(Work, Textual):
    @abstractmethod
    def work (self)-> 'Work': 
        pass
    @abstractmethod
    def as_dict(self) -> str: 
        pass
    @abstractmethod
    def as_string(self) -> str: 
        pass
    @abstractmethod
    def exercise(self)-> str: 
        pass
    @abstractmethod
    def workload_type(self)-> WorkloadType: 
        pass
   
   