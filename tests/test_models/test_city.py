#!/usr/bin/python3
"""Unittest module for City class"""

import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCityDocs(unittest.TestCase):
    """Tests documentation and style of City class"""

    def test_pep8_conformance_city(self):
        """Test that models/city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test module docstring"""
        self.assertIsNotNone(City.__doc__,
                             "city.py needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test City class docstring"""
        self.assertIsNotNone(City.__doc__,
                             "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")


class TestCity(unittest.TestCase):
    """Test the City class"""

    @classmethod
    def setUpClass(cls):
        """Setup for the test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Cleanup after the test"""
        del cls.city

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attributes_City(self):
        """Check if City has the required attributes"""
        attributes = ['id', 'created_at', 'updated_at', 'state_id', 'name']
        for attr in attributes:
            self.assertTrue(hasattr(self.city, attr))

    def test_is_subclass_City(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_attribute_types_City(self):
        """Test attribute types for City"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_save_City(self):
        """Test if the save method works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
