# import pytest

# from Exercise.Exercise import Exercise
# from Exercise.ExerciseExecution import ExerciseExecutionByTask
# from Exercise.ExerciseTask import ExerciseTask
# from Exercise.Step.ExerciseStep import ExerciseStep



# class TestExerciseExecutionByTask:
#     def test_exercise_execution_creation(self):
#         execution = ExerciseExecutionByTask (
#             ExerciseTask(
#                 Exercise('Отжимания'),
#                 25),
#         )
#     def test_execution(self):
#         execution = ExerciseExecutionByTask (
#             ExerciseTask(
#                 Exercise('Отжимания'),
#                 25))
#         execution.execute(
#             ExerciseStep (
#                 Exercise('Отжимания'), 
#                 3)
#         )
#     def test_remaind(self):
#         assert 25 == \
#             ExerciseExecutionByTask (
#                 ExerciseTask(
#                     Exercise('Отжимания'),
#                     25)) \
#                     .remaind()
#     def  test_remaind_after_execution_step(self):
#         exerciseExecution = ExerciseExecutionByTask (
#                 ExerciseTask(
#                     Exercise('Отжимания'),
#                     25))
#         exerciseExecution.execute(ExerciseStep(Exercise('Отжимания'), 5))
#         assert 20 == exerciseExecution.remaind()