# This file is placed in the Public Domain.


"static tables"


import unittest


from bigtalk.statics import NAMES


class TestStatic(unittest.TestCase):

    def test_names(self):
        self.assertTrue(NAMES)
