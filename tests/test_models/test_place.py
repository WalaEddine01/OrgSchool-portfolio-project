#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes
"""

from datetime import datetime
import inspect
import models
from models import class
from models.base_model import BaseModel
import pep8
import unittest
Place = class.Place


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Place class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.school_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_school(self):
        """Test that models/school.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/school.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_school(self):
        """Test that tests/test_models/test_school.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_school.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_school_module_docstring(self):
        """Test for the school.py module docstring"""
        self.assertIsNot(class.__doc__, None,
                         "school.py needs a docstring")
        self.assertTrue(len(class.__doc__) >= 1,
                        "school.py needs a docstring")

    def test_school_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_school_func_docstrings(self):
        """Test for the presence of docstrings in Place methods"""
        for func in self.school_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPlace(unittest.TestCase):
    """Test the Place class"""
    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        school = Place()
        self.assertIsInstance(school, BaseModel)
        self.assertTrue(hasattr(school, "id"))
        self.assertTrue(hasattr(school, "created_at"))
        self.assertTrue(hasattr(school, "updated_at"))

    def test_student_id_attr(self):
        """Test Place has attr student_id, and it's an empty string"""
        school = Place()
        self.assertTrue(hasattr(school, "student_id"))
        if models.storage_t == 'db':
            self.assertEqual(school.student_id, None)
        else:
            self.assertEqual(school.student_id, "")

    def test_admin_id_attr(self):
        """Test Place has attr admin_id, and it's an empty string"""
        school = Place()
        self.assertTrue(hasattr(school, "admin_id"))
        if models.storage_t == 'db':
            self.assertEqual(school.admin_id, None)
        else:
            self.assertEqual(school.admin_id, "")

    def test_name_attr(self):
        """Test Place has attr name, and it's an empty string"""
        school = Place()
        self.assertTrue(hasattr(school, "name"))
        if models.storage_t == 'db':
            self.assertEqual(school.name, None)
        else:
            self.assertEqual(school.name, "")

    def test_description_attr(self):
        """Test Place has attr description, and it's an empty string"""
        school = Place()
        self.assertTrue(hasattr(school, "description"))
        if models.storage_t == 'db':
            self.assertEqual(school.description, None)
        else:
            self.assertEqual(school.description, "")

    def test_number_rooms_attr(self):
        """Test Place has attr number_rooms, and it's an int == 0"""
        school = Place()
        self.assertTrue(hasattr(school, "number_rooms"))
        if models.storage_t == 'db':
            self.assertEqual(school.number_rooms, None)
        else:
            self.assertEqual(type(school.number_rooms), int)
            self.assertEqual(school.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test Place has attr number_bathrooms, and it's an int == 0"""
        school = Place()
        self.assertTrue(hasattr(school, "number_bathrooms"))
        if models.storage_t == 'db':
            self.assertEqual(school.number_bathrooms, None)
        else:
            self.assertEqual(type(school.number_bathrooms), int)
            self.assertEqual(school.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test Place has attr max_guest, and it's an int == 0"""
        school = Place()
        self.assertTrue(hasattr(school, "max_guest"))
        if models.storage_t == 'db':
            self.assertEqual(school.max_guest, None)
        else:
            self.assertEqual(type(school.max_guest), int)
            self.assertEqual(school.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test Place has attr price_by_night, and it's an int == 0"""
        school = Place()
        self.assertTrue(hasattr(school, "price_by_night"))
        if models.storage_t == 'db':
            self.assertEqual(school.price_by_night, None)
        else:
            self.assertEqual(type(school.price_by_night), int)
            self.assertEqual(school.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Place has attr latitude, and it's a float == 0.0"""
        school = Place()
        self.assertTrue(hasattr(school, "latitude"))
        if models.storage_t == 'db':
            self.assertEqual(school.latitude, None)
        else:
            self.assertEqual(type(school.latitude), float)
            self.assertEqual(school.latitude, 0.0)

    def test_longitude_attr(self):
        """Test Place has attr longitude, and it's a float == 0.0"""
        school = Place()
        self.assertTrue(hasattr(school, "longitude"))
        if models.storage_t == 'db':
            self.assertEqual(school.longitude, None)
        else:
            self.assertEqual(type(school.longitude), float)
            self.assertEqual(school.longitude, 0.0)

    @unittest.skipIf(models.storage_t == 'db', "not testing File Storage")
    def test_amenity_ids_attr(self):
        """Test Place has attr amenity_ids, and it's an empty list"""
        school = Place()
        self.assertTrue(hasattr(school, "amenity_ids"))
        self.assertEqual(type(school.amenity_ids), list)
        self.assertEqual(len(school.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_class" in new_d)
        for attr in p.__dict__:
            if attr is not "_sa_instance_class":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        school = Place()
        string = "[Place] ({}) {}".format(school.id, school.__dict__)
        self.assertEqual(string, str(school))
