from datetime import datetime

import src.service.mongo as MongoSvc


INP = {
    'str'  : 'value00',
    'int'  : 122,
    'date' : datetime(2011, 12, 13),
}

class Test:

    def test(self):
        d = INP; d['_id'] = datetime.now()  # add this field to have unique ObjectId in mongo
        MongoSvc.insert(document=d, collection_name='unittest-form')

    def test2(self):
        d = INP; d['_id'] = datetime.now()  # add this field to have unique ObjectId in mongo
        c = MongoSvc.connect(collection_name='unittest-form')  # c aka collection
        c.insert_one(d)
