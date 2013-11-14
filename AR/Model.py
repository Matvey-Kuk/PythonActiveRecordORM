import pymysql


class Model(object):

    table_name = ''

    table_columns = [
    ]

    def __init__(self):
        pass

    def save(self):
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