#!/usr/bin/python3
"""
TestStateDocs classes
"""

import unittest
import os
import pep8
import inspect
from models.state import State
from models.base_model import BaseModel


class TestStateDocs(unittest.TestCase):
    """Tests whether the documentation and style of State class"""
    @classmethod
    def setUpClass(cls):
        """Setting  up for the documentation tests"""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Test whether models/state.py follows to PEP8 style."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """Test whether tests/test_models/test_state.py follows to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """Test whether the state.py module has docstring"""
        self.assertIsNot(State.__doc__, None,
                         "state.py requires a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "state.py requires a docstring")

    def test_state_class_docstring(self):
        """Test whether the State class docstring"""
        self.assertIsNot(State.__doc__, None,
                         "State class requires a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class requires a docstring")

    def test_state_func_docstrings(self):
        """Test for presence of docstrings in State methods"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestState(unittest.TestCase):
    """Test the State class"""
    def setUp(self):
        """set up for test"""
        self.state = State()
        self.state.name = "CA"

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_is_subclass(self):
        """Test whether state is a subclass of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_name_attr(self):
        """Test whether State has attribute name,
        and it's as an empty string"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_to_dict_creates_dict(self):
        """test whether to_dict method
        creates a dictionary with proper attributes"""
        new_d = self.state.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in self.state.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test whether values in dict
        returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_d = self.state.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], self.state.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], self.state.updated_at.strftime(t_format))

    def test_str(self):
        """test whether the str method has the
        correct output"""
        string = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(string, str(self.state))


if __name__ == "__main__":
    unittest.main()
