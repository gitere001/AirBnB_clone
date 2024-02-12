#!/usr/bin/python3
"""
test model for class City
"""
from models.base_model import BaseModel
# import models
import unittest
from models.city import City
import os


class TestCity(unittest.TestCase):
    """
    class for testing City class
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
        # Create a city instance
        my_city = City()
        # Check if attributes are initialized correctly
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")

    def test_inheritance_from_base_model(self):
        """Test inheritance from BaseModel."""
        # Create a city instance
        my_city = City()
        # Check if City class inherits from BaseModel
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(my_city, City)

    def test_string_representation(self):
        """Test string representation."""
        # Create a City instance
        my_city = City(
            state_id="123",
            name="Florida",
        )
        str_my_city = str(my_city)
        # Test if "123" is present in the str representation
        self.assertIn("123", str_my_city)
        # Test if "Florida" is present in the str representation
        self.assertIn("Florida", str_my_city)

    def test_dictionary_representation(self):
        """Test dictionary representation."""
        # Create a City instance
        my_city = City()
        # Set attributes
        my_city.state_id = "123"
        my_city.name = "Florida"
        # Get dictionary representation
        city_dict = my_city.to_dict()
        # Check if dictionary contains expected key-value pairs
        self.assertEqual(city_dict["state_id"], "123")
        self.assertEqual(city_dict["name"], "Florida")

    def test_instance_creation_with_arguments(self):
        """Test instance creation with arguments."""
        # Create a City instance with arguments
        my_city = City(state_id="123", name="Florida")
        # Check if attributes are set correctly
        self.assertEqual(my_city.state_id, "123")
        self.assertEqual(my_city.name, "Florida")

    def test_instance_creation_with_dictionary(self):
        """Test instance creation with dictionary."""
        # Create a dictionary
        city_dict = {
            "state_id": "123",
            "name": "Florida",
            "__class__": "City",
        }
        # Create a City instance from the dictionary
        my_city = City(**city_dict)
        # Check if attributes are set correctly
        self.assertEqual(my_city.state_id, "123")
        self.assertEqual(my_city.name, "Florida")


if __name__ == "__main__":
    unittest.main()
