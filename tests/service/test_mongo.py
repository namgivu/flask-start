from datetime import datetime

import src.service.mongo as MongoSvc


class Test:

    def test(self):
        d = {
            'str'  : 'value00',
            'int'  : 122,
            'date' : datetime(2011, 12, 13),
        }
        MongoSvc.insert(document=d, collection_name='unittest-form')
