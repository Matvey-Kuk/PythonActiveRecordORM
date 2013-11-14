from Models.TableA import *
from Models.TableB import *


class Test(object):
    def __init__(self):
        self.test_save()

    @staticmethod
    def test_save():
        table_a = TableA()
        table_a.save()

test = Test