""" This script contains the unit tests for the Batch Calls script """

import unittest

from test_config import app_config


class TestStringMethods(unittest.TestCase):
    """
        We recommend running these unit tests using the
           file syntax:  python -m unittest test_batch_call
        To discover and run all unit tests:  python -m unittest
        To run the unit tests in a file:  python -m unittest test_batch_call
        To run a single test:  python -m unittest test_batch_call.TestStringMethods.test_dobatchcall
    """

    def test_dobatchcall(self):
        """ Call the do_batch_call method """
        from batch_call import do_batch_call
        self.assertEqual(do_batch_call(app_config['url'], app_config['af'],
                                       app_config['user'], app_config['password'], app_config['auth']), 207)


if __name__ == '__main__':
    unittest.main()
