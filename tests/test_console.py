"""Unit tests for the HBNBCommand class"""
import sys
import unittest
import os
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Contains unit tests for the HBNBCommand class"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

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
        self.assertTrue('[]' in output)

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

    def test_prompt(self):
        """
        Tests that the prompt is set to "(hbnb)".
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """
        Tests the behavior when an empty line is entered.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommandHelp(unittest.TestCase):
    """Contains unit tests for the HBNBCommand help messages."""

    def test_help_create(self):
        """
        Tests the help message for the 'create' command.
        """
        create = ("Create a new instance of a specified class.\n        "
                  "USAGE: create <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(create, output.getvalue().strip())

    def test_help_quit(self):
        """
        Tests the help message for the 'quit' command.
        """
        quit = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(quit, output.getvalue().strip())

    def test_help_EOF(self):
        """
        Tests the help message for the 'EOF' command.
        """
        eof = "Signal to exit the command loop."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(eof, output.getvalue().strip())

    def test_help_all(self):
        """
        Tests the help message for the 'all' command.
        """
        all = ("List all instances or instances of a specific class.\n        "
               "USAGE: all <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(all, output.getvalue().strip())

    def test_help_show(self):
        """
        Tests the help message for the 'show' command.
        """
        show = ("Display information about a specific instance.\n        "
                "USAGE: show <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(show, output.getvalue().strip())

    def test_help_destroy(self):
        """
        Tests the help message for the 'destroy' command.
        """
        destroy = ("Remove a specified instance.\n        "
                   "USAGE: show <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(destroy, output.getvalue().strip())

    def test_help_update(self):
        """
        Tests the help message for the 'update' command.
        """
        update = ("Update the attributes of a specified instance.\n        "
                  "USAGE: update <class name> <id> <attribute name> "
                  '"<attribute value>"')
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(update, output.getvalue().strip())

    def test_help_count(self):
        """
        Tests the help message for the 'count' command.
        """
        count = \
            ("Count the number of instances of a specified class.\n        "
                "USAGE: count <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(count, output.getvalue().strip())

    def test_help(self):
        """
        Tests the help message for the 'help' command.
        """
        help = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help, output.getvalue().strip())


class TestHBNBCommandCreate(unittest.TestCase):
    """Contains unit tests for the 'create' command in HBNBCommand."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_class_name_missing(self):
        """Tests behavior when the class name is missing."""
        msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_invalid_class_name(self):
        """Tests behavior when an invalid class name is provided."""
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create invalid"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_class_unknown_syntax_default(self):
        """Tests behavior with an unknown syntax for the 'create' command."""
        msg = "*** Unknown syntax: Invalid.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Invalid.create()"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_create_objects(self):
        """Tests the successful creation of objects for various classes."""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"User.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"State.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"City.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"Amenity.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"Place.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"Review.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())
