"""Unit tests for the State class."""
import unittest

from models.state import State


class TestState(unittest.TestCase):
    """Contains unit tests for the State class."""

    #  State object can be instantiated with no arguments
    def test_instantiate_with_no_arguments(self):
        state = State()
        self.assertIsInstance(state, State)

    #  State object can be instantiated with name argument
    def test_instantiate_with_name_argument(self):
        state = State(name="California")
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "California")

    #  State object name can be set to an empty string
    def test_set_name_to_empty_string(self):
        state = State()
        state.name = ""
        self.assertEqual(state.name, "")

    #  State object name can be set to a string with length 128
    def test_set_name_to_string_with_length_128(self):
        state = State()
        state.name = "A" * 128
        self.assertEqual(state.name, "A" * 128)

    #  State object name can be set to a string with length greater than 128
    def test_set_name_to_string_with_length_greater_than_128(self):
        state = State()
        state.name = "A" * 129
        self.assertEqual(state.name, "A" * 129)
