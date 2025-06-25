import pytest
from django.test import TestCase, Client
# from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from abc import ABC, abstractmethod
import requests

from Workout.app.workout_django.excercise_execution.views import HttpRepsWork

class Work(ABC):
    @abstractmethod
    def execute (self): pass
    def as_string(self): pass
    
class Textual(ABC):
    @abstractmethod
    def content() -> str: pass 

class RepsWork(Work, Textual):
    def __init__(self, title: str, reps: int):
        self._title = title
        self._reps = reps
    def execute (self): pass
    def content(self):
        return 'pullups 25 repetitions'
   
   
class TestWork():
    def test_reps_work_create(self):
        repsWork = RepsWork('pullups', 25)
        
    def test_RepsWork_execute(self):
        repsWork = RepsWork('pullups', 25)
        repsWork.execute()
        
    def test_work_as_string(self):
        work = RepsWork('pullups', 25)
        assert 'pullups 25 repetitions' == work.content()

class TestHttpTestWork():
    def test_reps_work_create(self):
        client = Client()
        # client.get("http://127.0.0.1:8000/excercise_execute/work/")
        client.reverse("http://127.0.0.1:8000/excercise_execute/work/")
        response = HttpRepsWork().execute()
        repsWork = HttpResponse(
            {RepsWork('pullups', 25)}
        )
        assert 'pullups 25 repetitions' == repsWork.execute().response.content.decode()