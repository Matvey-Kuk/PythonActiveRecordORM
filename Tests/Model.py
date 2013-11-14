import unittest

from Models.TableA import *
from AR.Exceptions import *


class Test(unittest.TestCase):

    def test_save(self):
        table_a = TableA()
        table_a.set_value('TableB_id', 123)
        table_a.save()

    def test_exceptions(self):
        table_a = TableA()
        with self.assertRaises(WrongValueException):
            table_a.set_value('id', 'abc')
        with self.assertRaises(WrongValueException):
            table_a.set_value('id', None)
        with self.assertRaises(WrongValueException):
            table_a.set_value('a', 'abc')