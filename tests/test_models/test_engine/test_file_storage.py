#!/usr/bin/python3
"""Unit tests for FileStorage module"""
import os.path
import unittest
import pep8
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def test_pep8_FileStorage(self):
        """Tests PEP8 style for file_storage.py"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_all_method(self):
        """Tests all() method of FileStorage"""
        self.assertTrue(type(storage.all()) is dict)

        # Pass arg to all() method
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_method(self):
        """Tests new() method of FileStorage"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        # Checks that the objects created above are stored already
        self.assertIn("BaseModel." + dummy_bm.id, storage.all().keys())
        self.assertIn(dummy_bm, storage.all().values())
        self.assertIn("User." + dummy_user.id, storage.all().keys())
        self.assertIn(dummy_user, storage.all().values())
        self.assertIn("State." + dummy_state.id, storage.all().keys())
        self.assertIn(dummy_state, storage.all().values())
        self.assertIn("Place." + dummy_place.id, storage.all().keys())
        self.assertIn(dummy_place, storage.all().values())
        self.assertIn("City." + dummy_city.id, storage.all().keys())
        self.assertIn(dummy_city, storage.all().values())
        self.assertIn("Amenity." + dummy_amenity.id, storage.all().keys())
        self.assertIn(dummy_amenity, storage.all().values())
        self.assertIn("Review." + dummy_review.id, storage.all().keys())
        self.assertIn(dummy_review, storage.all().values())

        # If more than one arg was passed, raise TypeError
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

        # If no arg is passed, raise AttributeError
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save_method(self):
        """Tests save() method of FileStorage"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        storage.save()

        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + dummy_bm.id, save_text)
            self.assertIn("User." + dummy_user.id, save_text)
            self.assertIn("State." + dummy_state.id, save_text)
            self.assertIn("Place." + dummy_place.id, save_text)
            self.assertIn("City." + dummy_city.id, save_text)
            self.assertIn("Amenity." + dummy_amenity.id, save_text)
            self.assertIn("Review." + dummy_review.id, save_text)

        # Pass arg to save() method
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method(self):
        """Tests reload() method of FileStorage"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        storage.save()
        storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + dummy_bm.id, objects)
        self.assertIn("User." + dummy_user.id, objects)
        self.assertIn("State." + dummy_state.id, objects)
        self.assertIn("Place." + dummy_place.id, objects)
        self.assertIn("City." + dummy_city.id, objects)
        self.assertIn("Amenity." + dummy_amenity.id, objects)
        self.assertIn("Review." + dummy_review.id, objects)

        # Pass arg to reload() method
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
