#!/usr/bin/python3
"""
Contains the TestAdminDocs classes
"""

from datetime import datetime
import inspect
import models
from models import admin
from models.base_model import BaseModel
import pep8
import unittest
Admin = admin.Admin


class TestAdminDocs(unittest.TestCase):
    """Tests to check the documentation and style of Admin class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.admin_f = inspect.getmembers(Admin, inspect.isfunction)

    def test_pep8_conformance_admin(self):
        """Test that models/admin.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/admin.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_admin(self):
        """Test that tests/test_models/test_admin.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_admin.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_admin_module_docstring(self):
        """Test for the admin.py module docstring"""
        self.assertIsNot(admin.__doc__, None,
                         "admin.py needs a docstring")
        self.assertTrue(len(admin.__doc__) >= 1,
                        "admin.py needs a docstring")

    def test_admin_class_docstring(self):
        """Test for the Student class docstring"""
        self.assertIsNot(Admin.__doc__, None,
                         "Admin class needs a docstring")
        self.assertTrue(len(Admin.__doc__) >= 1,
                        "Admin class needs a docstring")

    def test_admin_func_docstrings(self):
        """Test for the presence of docstrings in Admin methods"""
        for func in self.admin_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAdmin(unittest.TestCase):
    """Test the Admin class"""
    def test_is_subclass(self):
        """Test that Admin is a subclass of BaseModel"""
        admin = Admin()
        self.assertIsInstance(admin, BaseModel)
        self.assertTrue(hasattr(admin, "id"))
        self.assertTrue(hasattr(admin, "created_at"))
        self.assertTrue(hasattr(admin, "updated_at"))

    def test_email_attr(self):
        """Test that Admin has attr email, and it's an empty string"""
        admin = Admin()
        self.assertTrue(hasattr(admin, "email"))
        if models.storage_t == 'db':
            self.assertEqual(admin.email, None)
        else:
            self.assertEqual(admin.email, "")

    def test_password_attr(self):
        """Test that Admin has attr password, and it's an empty string"""
        admin = Admin()
        self.assertTrue(hasattr(admin, "password"))
        if models.storage_t == 'db':
            self.assertEqual(admin.password, None)
        else:
            self.assertEqual(admin.password, "")

    def test_first_name_attr(self):
        """Test that Admin has attr first_name, and it's an empty string"""
        admin = Admin()
        self.assertTrue(hasattr(admin, "first_name"))
        if models.storage_t == 'db':
            self.assertEqual(admin.first_name, None)
        else:
            self.assertEqual(admin.first_name, "")

    def test_last_name_attr(self):
        """Test that Admin has attr last_name, and it's an empty string"""
        admin = Admin()
        self.assertTrue(hasattr(admin, "last_name"))
        if models.storage_t == 'db':
            self.assertEqual(admin.last_name, None)
        else:
            self.assertEqual(admin.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Admin()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_class" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_class":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = Admin()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Admin")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        admin = Admin()
        string = "[Admin] ({}) {}".format(admin.id, admin.__dict__)
        self.assertEqual(string, str(admin))
