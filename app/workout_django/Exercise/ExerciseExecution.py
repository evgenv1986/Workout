from abc import ABC, abstractmethod
from multiprocessing.connection import Client

from django.shortcuts import render
from requests import request
from Exercise import Exercise
from Exercise.Task import Task
from Exercise.Step.ExerciseStep import ExerciseStep
from Exercise.Step.ExerciseSteps import ExerciseSteps
from excercise_execution.Work import Workload
from excercise_execution.Work import RepsWork
from excercise_execution.Work import Work

class TaskExecution(ABC):
    @abstractmethod
    def execute():pass
    
class TaskExecutionInputDataForm(TaskExecution):
    _task : Task
    _task_execution : 'ExerciseExecutionByTask'
    def __init__(self, task_execution: TaskExecution):
        self._task_execution = task_execution
    def execute(self, request):
        return render(request,
                'execution/workout/taskExecution/taskExecution.html',
                {'task_execution': self._task_execution,
                'work_execute': "execution/workout/exercise/step/step.html"})


class ExerciseExecutionByTask:
    _exerciseTask: Task
    _exerciseSteps: ExerciseSteps
    _works = []
    def __init__(self, exerciseTask: Task):
        self._exerciseTask = exerciseTask
        self._exerciseSteps = ExerciseSteps()
    def execute(self, exerciseStep: ExerciseStep):
        self._exerciseSteps.add(exerciseStep)
    def executeWork(self, work: Work):
        self._works.append(work)
    def remaind(self): 
        works_reps = 0
        for w in self._works:
            works_reps += int (w.work())
        return (
            self._exerciseTask.reps() - 
            # self._exerciseSteps.reps()
            works_reps
        )
    def as_json(self):
        return {
            'title': self._exerciseTask._exercise._title,
            'reps': len(self._works)}
    def executed(self):
        works_reps = 0
        for w in self._works:
            works_reps += int (w.work())
        return works_reps
    def task_work(self):
        return self._exerciseTask.reps()