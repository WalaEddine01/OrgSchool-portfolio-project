#!/usr/bin/python3
"""
Contains the TestTeacherDocs classes
"""

from datetime import datetime
import inspect
import models
from models import teacher
from models.base_model import BaseModel
import pep8
import unittest
Teacher = teacher.Teacher


class TestTeacherDocs(unittest.TestCase):
    """Tests to check the documentation and style of Teacher class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.teacher_f = inspect.getmembers(Teacher, inspect.isfunction)

    def test_pep8_conformance_teacher(self):
        """Test that models/teacher.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/teacher.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_teacher(self):
        """Test that tests/test_models/test_teacher.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_teacher.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_teacher_module_docstring(self):
        """Test for the teacher.py module docstring"""
        self.assertIsNot(teacher.__doc__, None,
                         "teacher.py needs a docstring")
        self.assertTrue(len(teacher.__doc__) >= 1,
                        "teacher.py needs a docstring")

    def test_teacher_class_docstring(self):
        """Test for the Teacher class docstring"""
        self.assertIsNot(Teacher.__doc__, None,
                         "Teacher class needs a docstring")
        self.assertTrue(len(Teacher.__doc__) >= 1,
                        "Teacher class needs a docstring")

    def test_teacher_func_docstrings(self):
        """Test for the presence of docstrings in Teacher methods"""
        for func in self.teacher_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestTeacher(unittest.TestCase):
    """Test the Teacher class"""
    def test_is_subclass(self):
        """Test if Teacher is a subclass of BaseModel"""
        teacher = Teacher()
        self.assertIsInstance(teacher, BaseModel)
        self.assertTrue(hasattr(teacher, "id"))
        self.assertTrue(hasattr(teacher, "created_at"))
        self.assertTrue(hasattr(teacher, "updated_at"))

    def test_school_id_attr(self):
        """Test Teacher has attr school_id, and it's an empty string"""
        teacher = Teacher()
        self.assertTrue(hasattr(teacher, "school_id"))
        if models.storage_t == 'db':
            self.assertEqual(teacher.school_id, None)
        else:
            self.assertEqual(teacher.school_id, "")

    def test_admin_id_attr(self):
        """Test Teacher has attr admin_id, and it's an empty string"""
        teacher = Teacher()
        self.assertTrue(hasattr(teacher, "admin_id"))
        if models.storage_t == 'db':
            self.assertEqual(teacher.admin_id, None)
        else:
            self.assertEqual(teacher.admin_id, "")

    def test_text_attr(self):
        """Test Teacher has attr text, and it's an empty string"""
        teacher = Teacher()
        self.assertTrue(hasattr(teacher, "text"))
        if models.storage_t == 'db':
            self.assertEqual(teacher.text, None)
        else:
            self.assertEqual(teacher.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Teacher()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_class" in new_d)
        for attr in r.__dict__:
            if attr is not "_sa_instance_class":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Teacher()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Teacher")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        teacher = Teacher()
        string = "[Teacher] ({}) {}".format(teacher.id, teacher.__dict__)
        self.assertEqual(string, str(teacher))
