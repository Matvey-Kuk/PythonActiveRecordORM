from AR.Model import *


class TableA(Model):

    table_name = 'tablea'

    table_columns = [
        'id',
        'TableB_id'
    ]

    def rules(self):
        return {
            'id': [
                'required',
                'numeric'
            ],
            'TableB_id': [
                'required',
                'numeric'
            ]
        }

    def __init__(self):
        pass