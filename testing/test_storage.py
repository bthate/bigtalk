# This file is placed in the Public Domain.


import os
import sys
import unittest


sys.path.insert(0, ".")


from bigtalk.objects import Object
from bigtalk.persist import Cache, Disk
from bigtalk.workdir import Workdir


import bigtalk.persist


Workdir.wdr = '.test'


ATTRS1 = (
    'Cache',
    'Disk'
)


class TestStorage(unittest.TestCase):

    def test_constructor(self):
        obj = Cache()
        self.assertTrue(type(obj), Cache)

    def test__class(self):
        obj = Cache()
        clz = obj.__class__()
        self.assertTrue('Cache' in str(type(clz)))

    def test_dirmodule(self):
        self.assertEqual(
                         dir(bigtalk.persist),
                         list(ATTRS1)
                        )

    def test_module(self):
        self.assertTrue(Cache().__module__, 'Cache')

    def test_save(self):
        obj = Object()
        opath = Disk.write(obj)
        self.assertTrue(os.path.exists(opath))
