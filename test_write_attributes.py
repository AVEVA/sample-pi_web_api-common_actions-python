""" This script contains the unit tests for the WriteAttributes Script """

import unittest

from test_config import app_config


class TestStringMethods(unittest.TestCase):
    """
        We recommend running these unit tests using the file syntax:
            python -m unittest test_write_attributes
        To discover and run all unit tests:  python -m unittest
        To run the unit tests in a file:  python -m unittest test_write_attributes
        To run a single test:
            python -m unittest test_write_attributes.TestStringMethods.test_writedataset
    """

    def test_writesinglevalue(self):
        """ Test the write_single_value method """
        from write_attributes import write_single_value
        self.assertEqual(write_single_value(app_config['url'],
                                            app_config['af'], app_config['user'], app_config['password'], app_config['auth']), 202)

    def test_writedataset(self):
        """ Test the write_data_set method """
        from write_attributes import write_data_set
        self.assertEqual(write_data_set(app_config['url'],
                                        app_config['af'], app_config['user'], app_config['password'], app_config['auth']), 202)

    def test_updateattributevalue(self):
        """ Test the update_attribute_value method """
        from write_attributes import update_attribute_value
        self.assertEqual(update_attribute_value(app_config['url'],
                                                app_config['af'], app_config['user'], app_config['password'], app_config['auth']), 204)


if __name__ == '__main__':
    unittest.main()
