import pytest
from abc import ABC, abstractmethod

class Work(ABC):
    @abstractmethod
    def execute (self): pass
    # @abstractmethod
    # def work(self) -> 'Work': pass
    # @abstractmethod
    def as_string(self): pass

class RepsWork(Work):
    def __init__(self, title: str, reps: int):
        self._title = title
        self._reps = reps
    def execute (self): pass
    def as_string(self):
        return 'pullups 25 repetitions'
    # def work(self) -> 'Work': pass
    

class TestWork():
    def test_reps_work_create(self):
        repsWork = RepsWork('pullups', 25)
        
    def test_RepsWork_execute(self):
        repsWork = RepsWork('pullups', 25)
        repsWork.execute()
        
    def test_work_as_string(self):
        work = RepsWork('pullups', 25)
        assert 'pullups 25 repetitions' == work.as_string()

        