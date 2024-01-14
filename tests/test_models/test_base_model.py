"""Unit tests for the BaseModel class."""
import os
import unittest
from datetime import datetime
from time import sleep

from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    """Contains unit tests for the BaseModel class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_base_model_instance_no_arguments(self):
        """
        Test that a BaseModel instance can be created with no arguments
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_base_models_args_types(self):
        """Tests the types of attributes after BaseModel instantiation"""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_base_model_instance_keyword_arguments(self):
        """
        Test that a BaseModel instance can be created with keyword arguments
        """
        base_model = BaseModel(created_at='2022-01-01T00:00:00.000')
        self.assertIsInstance(base_model, BaseModel)
        self.assertEqual(base_model.created_at, datetime(2022, 1, 1, 0, 0, 0))

    def test_base_model_init_with_kwargs(self):
        """Tests BaseModel initialization with keyword arguments"""
        data = {'id': '415b1fec-2336-4dfa-8254-3b9006da20f1',
                'created_at': '2024-01-14T12:00:00.000', 'name': 'ALX'}
        obj = BaseModel(**data)

        assert obj.id == '415b1fec-2336-4dfa-8254-3b9006da20f1'
        assert obj.created_at == datetime(2024, 1, 14, 12, 0, 0)
        assert obj.name == 'ALX'

    def test_base_moder_not_used_args(self):
        """Tests BaseModel instantiation with unused positional arguments"""
        base_model = BaseModel("415b1fec-2336-4dfa-8254-3b9006da20e3")

        self.assertIsInstance(base_model, BaseModel)
        self.assertNotEqual(base_model.id,
                            "415b1fec-2336-4dfa-8254-3b9006da20e3")

    def test_base_moder_with_None(self):
        """Tests BaseModel instantiation with None as an argument"""
        base_model = BaseModel(None)
        self.assertIsInstance(base_model, BaseModel)

    def test_base_model_str(self):
        """Tests the string representation of BaseModel instances"""

        obj = BaseModel()
        obj.id = "415swfec-4536-4dfa-8254-3b9006da20fa"
        date = datetime.now()
        obj.created_at = obj.updated_at = date
        obj.name = 'ALX'
        output = str(obj)

        self.assertIn("[BaseModel] (415swfec-4536-4dfa-8254-3b9006da20fa)",
                      output)
        self.assertIn("'id': '415swfec-4536-4dfa-8254-3b9006da20fa'", output)
        self.assertIn(f"'created_at': {repr(date)}", output)
        self.assertIn(f"'updated_at': {repr(date)}", output)
        self.assertIn("'name': 'ALX'", output)

    def test_base_model_instance_invalid_created_at(self):
        """
        Test that a BaseModel instance cannot be created with an
        invalid created_at
        """
        with self.assertRaises(ValueError):
            BaseModel(created_at='invalid_date')


class TestBaseModelSave(unittest.TestCase):
    """Contains tests related to the save method of BaseModel instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_method(self):
        """Tests the save method of BaseModel instances"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        sleep(0.1)
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_save_two_times(self):
        """
        Tests calling the save method twice and checking
        if updated_at is greater the second time
        """
        obj = BaseModel()
        sleep(0.1)
        first_updated_at = obj.updated_at
        obj.save()
        sleep(0.1)
        obj.save()
        second_updated_at = obj.updated_at
        self.assertGreater(second_updated_at, first_updated_at)

    def test_save_with_arg(self):
        """
        Tests calling the save method with an argument
        (expects a TypeError).
        """
        obj = BaseModel()
        old_updated_at = obj.updated_at
        sleep(0.1)
        with self.assertRaises(TypeError):
            obj.save(None)


class TestBaseModelToDict(unittest.TestCase):
    """Contains tests related to the to_dict method of BaseModel instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict_method(self):
        """Tests the to_dict method of BaseModel instances"""
        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_contents(self):
        """Tests the contents of the dictionary returned by to_dict"""
        obj = BaseModel()
        obj.id = "99283s39sn2v"
        new_dict = obj.to_dict()
        self.assertEqual(new_dict['id'], "99283s39sn2v")
        self.assertEqual(new_dict['__class__'], "BaseModel")

    def test_to_dict_with_arg(self):
        """
        Tests calling the to_dict method with an argument
        (expects a TypeError)
        """
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.to_dict(None)
