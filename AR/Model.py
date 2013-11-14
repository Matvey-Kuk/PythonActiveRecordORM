import pymysql

from AR.Exceptions import *


class Model(object):

    table_name = ''

    table_columns = [
    ]

    values_for_updating = {
    }

    def __init__(self):
        self.is_loaded_from_db = False
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='91.Wj', db='pyar')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def save(self):
        print(self.values_for_updating)
        if not self.is_loaded_from_db:
            sql = "INSERT INTO "
            sql += "`" + self.table_name + "` "
            sql += "("
            for key in self.values_for_updating:
                sql += "`" + key + "`"
            sql += ")"
            sql += "VALUES "
            sql += "("
            for key in self.values_for_updating:
                sql += "'" + str(self.values_for_updating[key]) + "'"
            sql += ")"
            self.cursor.execute(sql)
            self.connection.commit()

    def set_value(self, name='', value=''):
        if not (name in self.table_columns):
            raise WrongValueException('No such column in table.')
        self.check_value_allowed_by_rules(name, value)
        self.values_for_updating[name] = value

    def check_value_allowed_by_rules(self, name='', value=''):
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