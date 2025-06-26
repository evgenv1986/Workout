import pytest
import json

from Exercise.Exercise import DictionaryExercise, Exercise, IExercise, JsonExercise
from Exercise.Step.ExerciseStep import ExerciseStep


class TestExercise:
    def test_exercise(self):
        exercise = Exercise ('Отжимания')
        assert Exercise ('Отжимания').__eq__(exercise)
        
    def test_json_exercise(self):
        title = 'Отжимания'
        dict_string = {
            'title': 'Отжимания'
        }
        dictExercise = DictionaryExercise(dict_string)
        
        _json = json.dumps(dict_string, ensure_ascii=False, indent=4)
        jsonExercise = JsonExercise(_json)
               
        assert title == 'Отжимания'
        assert dict_string['title'] == 'Отжимания'
        assert dictExercise.title() == 'Отжимания'
        assert jsonExercise.title() == 'Отжимания'
        
        
    