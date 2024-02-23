#!/usr/bin/python3
"""
Contains the TestStudentDocs classes
"""

from datetime import datetime
import inspect
import models
from models import student
from models.base_model import BaseModel
import pep8
import unittest
Student = student.Student


class TestStudentDocs(unittest.TestCase):
    """Tests to check the documentation and style of Student class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.student_f = inspect.getmembers(Student, inspect.isfunction)

    def test_pep8_conformance_student(self):
        """Test that models/student.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/student.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_student(self):
        """Test that tests/test_models/test_student.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_student.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_student_module_docstring(self):
        """Test for the student.py module docstring"""
        self.assertIsNot(student.__doc__, None,
                         "student.py needs a docstring")
        self.assertTrue(len(student.__doc__) >= 1,
                        "student.py needs a docstring")

    def test_student_class_docstring(self):
        """Test for the Student class docstring"""
        self.assertIsNot(Student.__doc__, None,
                         "Student class needs a docstring")
        self.assertTrue(len(Student.__doc__) >= 1,
                        "Student class needs a docstring")

    def test_student_func_docstrings(self):
        """Test for the presence of docstrings in Student methods"""
        for func in self.student_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestStudent(unittest.TestCase):
    """Test the Student class"""
    def test_is_subclass(self):
        """Test that Student is a subclass of BaseModel"""
        student = Student()
        self.assertIsInstance(student, BaseModel)
        self.assertTrue(hasattr(student, "id"))
        self.assertTrue(hasattr(student, "created_at"))
        self.assertTrue(hasattr(student, "updated_at"))

    def test_name_attr(self):
        """Test that Student has attribute name, and it's an empty string"""
        student = Student()
        self.assertTrue(hasattr(student, "name"))
        if models.storage_t == 'db':
            self.assertEqual(student.name, None)
        else:
            self.assertEqual(student.name, "")

    def test_class_id_attr(self):
        """Test that Student has attribute class_id, and it's an empty string"""
        student = Student()
        self.assertTrue(hasattr(student, "class_id"))
        if models.storage_t == 'db':
            self.assertEqual(student.class_id, None)
        else:
            self.assertEqual(student.class_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = Student()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_class" in new_d)
        for attr in c.__dict__:
            if attr is not "_sa_instance_class":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = Student()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "Student")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        student = Student()
        string = "[Student] ({}) {}".format(student.id, student.__dict__)
        self.assertEqual(string, str(student))
