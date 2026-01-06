# This file is placed in the Public Domain.


import unittest


from bigtalk.brokers import shutdown


class TestShutdown(unittest.TestCase):

    def test_shutdown(self):
        shutdown()
