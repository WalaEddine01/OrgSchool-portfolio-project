#!/usr/bin/python3
"""
Contains the TestClassDocs classes
"""

from datetime import datetime
import inspect
import models
from models import class
from models.base_model import BaseModel
import pep8
import unittest
Class = class.Class


class TestClassDocs(unittest.TestCase):
    """Tests to check the documentation and style of Class class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.class_f = inspect.getmembers(Class, inspect.isfunction)

    def test_pep8_conformance_class(self):
        """Test that models/class.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/class.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_class(self):
        """Test that tests/test_models/test_class.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_class.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_module_docstring(self):
        """Test for the class.py module docstring"""
        self.assertIsNot(class.__doc__, None,
                         "class.py needs a docstring")
        self.assertTrue(len(class.__doc__) >= 1,
                        "class.py needs a docstring")

    def test_class_class_docstring(self):
        """Test for the Class class docstring"""
        self.assertIsNot(Class.__doc__, None,
                         "Class class needs a docstring")
        self.assertTrue(len(Class.__doc__) >= 1,
                        "Class class needs a docstring")

    def test_class_func_docstrings(self):
        """Test for the presence of docstrings in Class methods"""
        for func in self.class_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestClass(unittest.TestCase):
    """Test the Class class"""
    def test_is_subclass(self):
        """Test that Class is a subclass of BaseModel"""
        class = Class()
        self.assertIsInstance(class, BaseModel)
        self.assertTrue(hasattr(class, "id"))
        self.assertTrue(hasattr(class, "created_at"))
        self.assertTrue(hasattr(class, "updated_at"))

    def test_name_attr(self):
        """Test that Class has attribute name, and it's as an empty string"""
        class = Class()
        self.assertTrue(hasattr(class, "name"))
        if models.storage_t == 'db':
            self.assertEqual(class.name, None)
        else:
            self.assertEqual(class.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = Class()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_class" in new_d)
        for attr in s.__dict__:
            if attr is not "_sa_instance_class":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = Class()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "Class")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        class = Class()
        string = "[Class] ({}) {}".format(class.id, class.__dict__)
        self.assertEqual(string, str(class))
