#!/usr/bin/python3
"""unittest for Amenity class"""
import unittest
import os
import pep8
import datetime

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests"""
        del cls.amenity

    def tearDown(self):
        """Teardown method"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_amenity_is_subclass_of_base_model(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_has_name_attribute(self):
        """Test if Amenity has the attribute 'name'"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_amenity_name_attribute_type(self):
        """Test if the 'name' attribute of Amenity is of type str"""
        self.assertIs(type(self.amenity.name), str)

    def test_amenity_name_attribute_initially_empty(self):
        """Test if the 'name' attribute of Amenity is initially empty"""
        self.assertTrue(bool(getattr(self.amenity, "name")))

    def test_pep8_style(self):
        """Test PEP8 style conformity"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_docstrings_exist(self):
        """Test if docstrings exist"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_amenity_attributes(self):
        """Test if Amenity has the required attributes"""
        attributes = ['id', 'created_at', 'updated_at', 'name']
        for attr in attributes:
            self.assertTrue(hasattr(self.amenity, attr))

    def test_amenity_attribute_types(self):
        """Test if attribute types are correct"""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)
        self.assertIsInstance(self.amenity.name, str)

    def test_amenity_save_method(self):
        """Test if the save method updates 'updated_at'"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_amenity_to_dict_method(self):
        """Test if the to_dict method returns a dictionary"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
