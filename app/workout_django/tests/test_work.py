from django.test import Client
import pytest

from Exercise.Step import ExerciseStep
from Workout.app.workout_django import Exercise
from excercise_execution.Work import RepsWork, WorkImp
from excercise_execution.Work.Workload import MinutesWorkloadType, RepsWorkload, MinutesWorkload, Workload
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workout_django.settings')

# import django
# django.setup()

# from django.test import TestCase, Client
# from django.urls import reverse

# from urllib import request
# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from abc import ABC, abstractmethod
# import requests

# from excercise_execution.views import WorkHttpGet, RepsWork

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
     
class TestWorkloadType:
    def test_workload_as_string(self):
        reps_workload = RepsWorkload()
        assert "Повторения" == reps_workload.title()
        
        time_workload = MinutesWorkload()
        assert "Минут" == time_workload.title()
        
       
class TestWork:
    def test_reps_work_create(self):
        repsWork = RepsWork('pullups', 25)
        
    def test_RepsWork_execute(self):
        repsWork = RepsWork('pullups', 25)
        repsWork.work()
        
    def test_work_as_string(self):
        work = RepsWork('pullups', 25)
        assert 'pullups 25 repetitions' == work.as_string()

class TestWorkload:
    def test_create_reps_workload(self):
        repsWorkload = RepsWorkload(25)
        assert "25 повторени(я/й/е)" == repsWorkload.as_string()
    def test_create_time_workload(self):
        time_workload = MinutesWorkload(2)
        assert "2 минут(а/ы)" == time_workload.as_string()
    def test_equals(self):
        assert MinutesWorkload(2).__eq__(MinutesWorkload(2))
    def test_addition_workload(self):        
        time_work_2 = MinutesWorkload(2)
        time_work_3 = MinutesWorkload(3)
        time_work_2.add(time_work_3)
        assert MinutesWorkload(5).__eq__(time_work_2.total_work_value())
        # assert MinutesWorkload(5).value() == time_work_2.total_work().value()
    def test_next_in_work(self):
        time_work_2 = MinutesWorkload(2)
        next = time_work_2.next()
        assert "Empty workload" == next.title()
    def test_total_work(self):
        time_work_2 = MinutesWorkload(2)
        assert 2 == time_work_2.total_work_value()
    
class TestMergedWorkloadAndSeparatedWorkloadTypes:
    def test_merge_workload_into_one_class_and_separate_type_workloads(self):
        workload = Workload(2, MinutesWorkloadType())
        assert "2 минут(а/ы)" == workload.as_string()
        
 
        

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