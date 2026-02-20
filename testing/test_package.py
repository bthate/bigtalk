# This file is placed in the Public Domain.


"package"


import unittest


from bigtalk.package import Mods


class TestPackage(unittest.TestCase):

    def test_init(self):
        Mods.init("test", ".test")
        self.assertTrue("test" in Mods.dirs)
