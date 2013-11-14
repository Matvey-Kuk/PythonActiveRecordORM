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
            raise WrongValueException('No such column in table.')
        self.check_value_allowed(name, value)

    def check_value_allowed(self, name='', value=''):
        rules = self.rules()
        if name in rules:
            if 'numeric' in rules[name]:
                if not isinstance(value, int):
                    raise WrongValueException('Value must be numeric.')
            if 'required' in rules[name]:
                if value is None:
                    raise WrongValueException('Value is required.')
        else:
            return True

    def rules(self):
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