
from abc import ABC, abstractmethod


class Work(ABC):
    @abstractmethod
    def work (self)-> 'Work': pass
    
class Textual(ABC):
    @abstractmethod
    def as_json(self) -> str: pass 
    @abstractmethod
    def as_string(self) -> str: pass 
    


class TextualWork(Work, Textual):
    @abstractmethod
    def work (self)-> 'Work': pass
    @abstractmethod
    def as_json(self) -> str: pass
    @abstractmethod
    def as_string(self) -> str: pass
   
   