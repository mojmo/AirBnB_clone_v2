"""Unit tests for the HBNBCommand class"""
import sys
import unittest
import os
from io import StringIO

from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Contains unit tests for the HBNBCommand class"""

    def test_do_quit(self):
        """
        Test that the 'do_quit' method returns True when called.
        """
        cmd = HBNBCommand()
        result = cmd.do_quit("")
        self.assertTrue(result)

    def test_do_EOF(self):
        """
        Test that the 'do_EOF' method returns True when called.
        """
        cmd = HBNBCommand()
        result = cmd.do_EOF("")
        self.assertTrue(result)

    def test_emptyline(self):
        """
        Test that the 'emptyline' method does not raise any errors when called.
        """
        cmd = HBNBCommand()
        try:
            cmd.emptyline()
        except Exception as e:
            self.fail(f"emptyline raised an exception: {e}")

    def test_do_create_no_class_name(self):
        """
        Test that the 'do_create' method prints an error message
        if no class name is provided.
        """
        cmd = HBNBCommand()
        # Save a reference to the original standard output
        original_stdout = sys.stdout
        # Redirect standard output to a new StringIO object
        sys.stdout = StringIO()
        cmd.do_create("")
        # Retrieve the output from the StringIO object
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout  # Restore the original standard output
        self.assertTrue('** class name missing **' in output)

    def test_do_create_invalid_class_name(self):
        """
        Test that the 'do_create' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_create("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_do_show_no_class_name(self):
        """
        Test that the 'do_show' method prints an error message
        if no class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_show("")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class name missing **' in output)

    def test_do_show_invalid_class_name(self):
        """
        Test that the 'do_show' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_show("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_do_destroy_no_class_name(self):
        """
        Test that the 'do_destroy' method prints an error message
        if no class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_destroy("")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class name missing **' in output)

    def test_do_destroy_invalid_class_name(self):
        """
        Test that the 'do_destroy' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_destroy("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_do_all_no_class_name(self):
        """
        Test that the 'do_all' method prints all instances
        if no class name is provided.
        """
        cmd = HBNBCommand()
        cmd.do_all("")
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_all("")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertFalse('[]' in output)

    def test_do_all_invalid_class_name(self):
        """
        Test that the 'do_all' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_all("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_do_update_no_class_name(self):
        """
        Test that the 'do_update' method prints an error message
        if no class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_update("")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class name missing **' in output)

    def test_do_update_invalid_class_name(self):
        """
        Test that the 'do_update' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_update("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_default_unknown_command(self):
        """
        Test that the 'default' method prints an error message
        if an unknown command is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.default("UnknownCommand")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('*** Unknown syntax: UnknownCommand' in output)
