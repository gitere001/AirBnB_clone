#!/usr/bin/python3
"""
test model for class Amenity
"""
from models.base_model import BaseModel
# import models
import unittest
from models.amenity import Amenity
import os


class TestCity(unittest.TestCase):
    """
    class for testing Amenity class
    """

    def setUp(self):
        """Set up testing environment."""
        # Create a temporary file to save data
        self.my_test_file = "my_test_file.json"

    def tearDown(self):
        """Clean up after testing."""
        # Remove the temporary file after testing
        if os.path.exists(self.my_test_file):
            os.remove(self.my_test_file)

    def test_attribute_initialization(self):
        """Test attribute initialization."""
        # Create a amenity instance
        my_amenity = Amenity()
        # Check if attributes are initialized correctly
        self.assertEqual(my_amenity.name, "")

    def test_inheritance_from_base_model(self):
        """Test inheritance from BaseModel."""
        # Create Amenity instance
        my_amenity = Amenity()
        # Check if Amenity class inherits from BaseModel
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(my_amenity, Amenity)

    def test_string_representation(self):
        """Test string representation."""
        # Create Amenity instance
        my_amenity = Amenity(name="parking")
        str_my_amenity = str(my_amenity)
        # Test if "name" is present in the str representation
        self.assertIn("name", str_my_amenity)

    def test_dictionary_representation(self):
        """Test dictionary representation."""
        # Create Amenity instance
        my_amenity = Amenity()
        # Set attributes
        my_amenity.name = "parking"
        # Get dictionary representation
        amenity_dict = my_amenity.to_dict()
        # Check if dictionary contains expected key-value pairs
        self.assertEqual(amenity_dict["name"], "parking")

    def test_instance_creation_with_arguments(self):
        """Test instance creation with arguments."""
        # Create a City instance with arguments
        my_amenity = Amenity(name="parking")
        # Check if attributes are set correctly
        self.assertEqual(my_amenity.name, "parking")

    def test_instance_creation_with_dictionary(self):
        """Test instance creation with dictionary."""
        # Create a dictionary
        amenity_dict = {"name": "parking"}
        # Create a City instance from the dictionary
        my_amenity = Amenity(**amenity_dict)
        # Check if attributes are set correctly
        self.assertEqual(my_amenity.name, "parking")


if __name__ == "__main__":
    unittest.main()
