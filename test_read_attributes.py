""" This script contains the unit tests for the ReadAttributes Script """

import unittest

from test_config import app_config


class TestStringMethods(unittest.TestCase):
    """
        We recommend running these unit tests using the file syntax:
            python -m unittest test_read_attributes
        To discover and run all unit tests:  python -m unittest
        To run the unit tests in a file:  python -m unittest test_read_attributes
        To run a single test:
            python -m unittest test_read_attributes.TestStringMethods.test_readattributesnapshot
    """

    def test_readattributesnapshot(self):
        """ Test the read_attribute_snapshot method """
        from read_attributes import read_attribute_snapshot
        self.assertEqual(read_attribute_snapshot(app_config['url'],
                                                 app_config['af'], app_config['user'], app_config['password'], app_config['auth']), 200)

    def test_readattributestream(self):
        """ Test the read_attribute_stream method """
        from read_attributes import read_attribute_stream
        self.assertEqual(read_attribute_stream(app_config['url'],
                                               app_config['af'], app_config['user'], app_config['password'], app_config['auth']), 200)

    def test_readattributeselectedfields(self):
        """ Test the read_attribute_selected_fields method """
        from read_attributes import read_attribute_selected_fields
        self.assertEqual(read_attribute_selected_fields(app_config['url'],
                                                        app_config['af'],
                                                        app_config['user'], app_config['password'], app_config['auth']), 200)


if __name__ == '__main__':
    unittest.main()
