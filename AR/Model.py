import pymysql

from AR.Exceptions.WrongValueException import *


class Model(object):

    table_name = ''

    table_columns = [
    ]

    values = {
    }

    def __init__(self):
        pass

    def save(self):
        pass

    def set_value(self, name='', value=''):
        if not (name in self.table_columns):
            raise WrongValueException

    def check_value_allowed(self, name='', value=''):
        pass

    @staticmethod
    def rules():
        return {
        }

    @staticmethod
    def relations():
        return {
        }

    def delete(self):
        pass

    @staticmethod
    def find():
        pass