import unittest
from datetime import datetime
from copy import deepcopy

import src.service.mongo as MongoSvc


MONGO_TEST_COLLECTION='unittest-form'

INP = {
    'str'  : 'value00',
    'int'  : 122,
    'date' : datetime(2011, 12, 13),
}

class Test(unittest.TestCase):

    def setUp(self):
        # ensure each testcase starts with fresh collection
        c=MongoSvc.connect(MONGO_TEST_COLLECTION); c.drop()  # c aka collection


    #region test insert
    def test(self):
        self._test_insert()


    def _test_insert(self):
        d = INP; d['_id'] = datetime.now()  # add this field to have unique ObjectId in mongo  # d aka document
        MongoSvc.insert(d, MONGO_TEST_COLLECTION)


    def test_insert2(self):
        d = INP; d['_id'] = datetime.now()  # add this field to have unique ObjectId in mongo
        c = MongoSvc.connect(MONGO_TEST_COLLECTION)  # c aka collection
        c.insert_one(d)

    #endregion test insert


    def test_query(self):
        c = MongoSvc.connect(MONGO_TEST_COLLECTION)  # c aka collection

        # create fixture
        d=deepcopy(INP); c.insert_one(d)  # d aka document

        # testee code
        ri_all = c.find({})  # ri_all aka all_row_as_iterator

        # assert
        r_all  = list(ri_all)  # convert to
        assert len(r_all)==1
        r = r_all[0]
        r.pop('_id')
        assert r == INP
