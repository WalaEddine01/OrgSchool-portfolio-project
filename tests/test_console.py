#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import inspect
import pycodestyle
import unittest
ORGCommand = console.ORGCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_ORGCommand_class_docstring(self):
        """Test for the ORGCommand class docstring"""
        self.assertIsNot(ORGCommand.__doc__, None,
                         "ORGCommand class needs a docstring")
        self.assertTrue(len(ORGCommand.__doc__) >= 1,
                        "ORGCommand class needs a docstring")
