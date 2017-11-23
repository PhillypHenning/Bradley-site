import datetime

from django.test import TestCase


class TestingTravis(TestCase):
    """TestingTravis"""
    def this_test_should_pass(self):
        """Pass test"""
        pass

    def this_test_should_also_pass(self):
        """Pass test"""
        pass

    def this_test_will_fail(self):
        """Fail test"""
        n = 1
        if n < 1:
            pass
