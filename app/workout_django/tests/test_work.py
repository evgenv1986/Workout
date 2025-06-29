import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workout_django.settings')

import django
django.setup()

from django.test import TestCase, Client
from django.urls import reverse

import pytest
from django.test import TestCase, Client
# from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from abc import ABC, abstractmethod
import requests

from excercise_execution.views import HttpWork, RepsWork

# class Work(ABC):
#     @abstractmethod
#     def execute (self): pass
#     def as_string(self): pass
    
# class Textual(ABC):
#     @abstractmethod
#     def content() -> str: pass 

# class RepsWork(Work, Textual):
#     def __init__(self, title: str, reps: int):
#         self._title = title
#         self._reps = reps
#     def execute (self): pass
#     def content(self):
#         return 'pullups 25 repetitions'
   
   
class TestWork():
    def test_reps_work_create(self):
        repsWork = RepsWork('pullups', 25)
        
    def test_RepsWork_execute(self):
        repsWork = RepsWork('pullups', 25)
        repsWork.work()
        
    def test_work_as_string(self):
        work = RepsWork('pullups', 25)
        assert 'pullups 25 repetitions' == work.as_string()
        

class TestHttpTestWork():
    def test_reps_work_create(self):
        client = Client(enforce_csrf_checks=False)
        url = '/excercise_execute/work/' 
        data = {'exercise': 'pullups', 'reps': 25}
        response = client.post(
            url,
            data=data,
            content_type='application/json'
        )
        response_data = response.json()
        assert 200 == response.status_code  # Или другой ожидаемый код
        assert 'pullups' == response.json()['exercise']
        assert 25 == response.json()['reps']
                    
    def test_excercise_execute_show_input_form(self):
        client = Client(enforce_csrf_checks=False)
        url = '/excercise_execute/work/' 
        response = client.get(url) 
        assert response.status_code.__eq__(200)