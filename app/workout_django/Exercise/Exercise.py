from abc import ABC, abstractmethod
import json


class IExercise(ABC):
    @abstractmethod
    def title(self): 
        pass


class Exercise(IExercise):
    _title: str
    def __init__(self, title: str):
        self._title = title
    def __eq__(self, other: 'Exercise'):
        return other._title.__eq__(self._title)
    def to_dict(self):
        return {'title': self._title}
    def title(self):
        return self._title

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'])
    

class DictionaryExercise(IExercise):
    _dicty: dict
    def __init__(self, dicty):
        self._dicty = dicty
    def title(self):
        return self._dicty['title']

class JsonExercise(IExercise):
    _json: json
    def __init__(self, json_: json):
        self._json = json_
    def title(self):
        return json.loads(self._json)['title']
        
        