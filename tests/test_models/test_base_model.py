#!/usr/bin/python3
"""Test module for base_model"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """A class for testing base_model"""
    def test_init(self):
        """Testing init function"""
        mod1 = BaseModel()

        self.assertIsNotNone(mod1.id)
        self.assertIsNotNone(mod1.created_at)
        self.assertIsNotNone(mod1.updated_at)

    def test_save(self):
        """Testing create_at and update_at if they are working"""
        mod1 = BaseModel()

        initial_update = mod1.updated_at

        current_update = mod1.save()

        self.assertNotEqual(initial_update, current_update)

    def test_to_dict(self):
        """Testing if the method is displaying the correct format"""
        mod1 = BaseModel()
        mod1_dict = mod1.to_dict()
        self.assertIsInstance(mod1_dict, dict)

        self.assertEqual(mod1_dict["__class__"], "BaseModel")
        self.assertEqual(mod1_dict["id"], mod1.id)
        self.assertEqual(mod1_dict["created_at"], mod1.created_at.isoformat())
        self.assertEqual(mod1_dict["updated_at"], mod1.updated_at.isoformat())

    def test_str(self):
        """Testing for string representation of the object"""
        mod1 = BaseModel()

        self.assertTrue(str(mod1).startswith('[BaseModel]'))
        self.assertIn(str(mod1.id), str(mod1))
        self.assertIn(str(mod1.__dict__), str(mod1))


if __name__ == "__main__":
    unittest.main()
