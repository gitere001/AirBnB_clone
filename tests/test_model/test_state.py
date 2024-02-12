#!/usr/bin/python3
"""
test model for class State
"""
from models.base_model import BaseModel
# import models
import unittest
from models.state import State
import os


class TestCity(unittest.TestCase):
    """
    class for testing State class
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
        # Create a State instance
        my_state = State()
        # Check if attributes are initialized correctly
        self.assertEqual(my_state.name, "")

    def test_inheritance_from_base_model(self):
        """Test inheritance from BaseModel."""
        # Create State instance
        my_state = State()
        # Check if State class inherits from BaseModel
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(my_state, State)

    def test_string_representation(self):
        """Test string representation."""
        # Create State instance
        my_state = State(name="Utah")
        str_my_state = str(my_state)
        # Test if "name" is present in the str representation
        self.assertIn("name", str_my_state)

    def test_dictionary_representation(self):
        """Test dictionary representation."""
        # Create State instance
        my_state = State()
        # Set attributes
        my_state.name = "Utah"
        # Get dictionary representation
        state_dict = my_state.to_dict()
        # Check if dictionary contains expected key-value pairs
        self.assertEqual(state_dict["name"], "Utah")

    def test_instance_creation_with_arguments(self):
        """Test instance creation with arguments."""
        # Create State instance with arguments
        my_state = State(name="Utah")
        # Check if attributes are set correctly
        self.assertEqual(my_state.name, "Utah")

    def test_instance_creation_with_dictionary(self):
        """Test instance creation with dictionary."""
        # Create a dictionary
        state_dict = {"name": "Utah"}
        # Create a City instance from the dictionary
        my_state = State(**state_dict)
        # Check if attributes are set correctly
        self.assertEqual(my_state.name, "Utah")


if __name__ == "__main__":
    unittest.main()
