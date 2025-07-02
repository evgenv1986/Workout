from Exercise.Step.ExerciseStep import ExerciseStep
from excercise_execution import Work


class Works:
    _next_work: Work
    # _works: list
    def __init__(self):
        self._works = []
    def add(self, work: Work):
        self._works.append (work)
        pass
    def reps(self)-> int:
        sum: int = 0
        for work in self._works:
            sum += int (work.reps())
        return sum
    def count(self):
        return len(self._works)