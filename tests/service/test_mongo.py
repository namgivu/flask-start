#TODO extract this test into pymongo-start repo

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
        d = deepcopy(INP); d['_id'] = datetime.now()  # add this field to have unique ObjectId in mongo  # d aka document
        MongoSvc.insert(d, MONGO_TEST_COLLECTION)


    def test_insert2(self):
        d = deepcopy(INP); d['_id'] = datetime.now()  # add this field to have unique ObjectId in mongo
        c = MongoSvc.connect(MONGO_TEST_COLLECTION)  # c aka collection
        c.insert_one(d)

    #endregion test insert


    #region test query

    def test_query1(self):
        c = MongoSvc.connect(MONGO_TEST_COLLECTION)  # c aka collection

        # create fixture
        d=deepcopy(INP); c.insert_one(d)  # d aka document

        # testee code
        ri_all = c.find({})  # ri_all aka all_row_as_iterator

        # assert
        r_all = list(ri_all)  # convert to list
        assert len(r_all)==1
        r = r_all[0]
        r.pop('_id')
        assert r == deepcopy(INP)


    def test_query2(self):
        c = MongoSvc.connect(MONGO_TEST_COLLECTION)  # c aka collection

        # create fixture
        d1=deepcopy(INP); d1['_id']=1; c.insert_one(d1)  # dx aka document
        d2=deepcopy(INP); d2['_id']=2; c.insert_one(d2)

        # testee code
        ri=c.find({});        l=list(ri); assert len(l)==2  # ri_all aka all_row_as_iterator
        ri=c.find({'_id':1}); l=list(ri); assert len(l)==1; r=l[0]; assert r == d1  # l aka list

    #endregion test query
