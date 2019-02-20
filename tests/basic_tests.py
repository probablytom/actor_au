import unittest
import functools
from actor_au import *

class PatternMatchingTests(unittest.TestCase):
    def setUp(self):
        self.actor = PatternMatchingActor()

    def test_performs_correct_action_on_message(self):
        def action(some_dict):
            some_dict['val'] = True
        dict_to_change = dict()

        action_to_perform = functools.partial(action, dict_to_change)
        self.actor.register_message_to_task('act', action_to_perform)
        self.actor.recieve_message('act')

        task_generator = self.actor.yield_tasks()
        next_action = next(task_generator)

        self.assertEquals(next_action, action_to_perform)

    def test_performs_when_given_message(self):
        def action(some_dict):
            some_dict['val'] = True
        dict_to_change = dict()

        action_to_perform = functools.partial(action, dict_to_change)
        self.actor.register_message_to_task('act', action_to_perform)
        self.actor.recieve_message('act')

        performance = self.actor.perform()
        next(performance)  # Should run action_to_perform

        self.assertTrue('val' in dict_to_change.keys())
