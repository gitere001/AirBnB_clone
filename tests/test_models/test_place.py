#!/usr/bin/python3
"""
Test module for class Place
"""
import os
import unittest
import models
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Class for testing class Place
    """
    def setUp(self):
        # Creating a temporary file to save
        self.my_test_file = "my_test_file.json"
        models.storage.__file_path = self.my_test_file
        models.storage.save()

    def tearDown(self):
        # Remove previously created file after use
        if os.path.exists(self.my_test_file):
            os.remove(self.my_test_file)

    def test_place_attributes(self):
        # Creating a new Place instance
        my_place = Place()
        # Check if attribute 'city_id' is an empty string
        self.assertEqual(my_place.city_id, "")
        # Check if attribute 'user_id' is an empty string
        self.assertEqual(my_place.user_id, "")
        # Check if attribute 'name' is an empty string
        self.assertEqual(my_place.name, "")
        # Check if attribute 'description' is an empty string
        self.assertEqual(my_place.description, "")
        # Check if attribute 'number_rooms' is 0
        self.assertEqual(my_place.number_rooms, 0)
        # Check if attribute 'number_bathrooms' is 0
        self.assertEqual(my_place.number_bathrooms, 0)
        # Check if attribute 'max_guest' is 0
        self.assertEqual(my_place.max_guest, 0)
        # Check if attribute 'price_by_night' is 0
        self.assertEqual(my_place.price_by_night, 0)
        # Check if attribute 'latitude' is 0.0
        self.assertEqual(my_place.latitude, 0.0)
        # Check if attribute 'longitude' is 0.0
        self.assertEqual(my_place.longitude, 0.0)
        # Check if attribute 'amenity_ids' is an empty list
        self.assertEqual(my_place.amenity_ids, [])

    def test_place_inheritance_from_base_class(self):
        # Creating a new Place instance
        my_place = Place()
        # Testing if Place class is a subclass of BaseModel class
        self.assertEqual(issubclass(Place, BaseModel), True)
        # Additional assertion to check if my_place is an instance of BaseModel
        self.assertIsInstance(my_place, Place)

    def test_place_str_representation(self):
        # Creating a new Place instance
        my_place = Place()
        # Setting attributes of Place instance
        my_place.city_id = "my_city_id"
        my_place.user_id = "my_user_id"
        my_place.name = "My Place"
        my_place.description = "My Description"
        my_place.number_rooms = 5
        my_place.number_bathrooms = 3
        my_place.max_guest = 10
        my_place.price_by_night = 100
        my_place.latitude = 50.123
        my_place.longitude = -100.321
        my_place.amenity_ids = ["amenity_id1", "amenity_id2"]
        # Getting str representation of Place instance
        str_place = str(my_place)
        # Test if "Place" is present in the str representation
        self.assertIn("Place", str_place)
        # Test if city_id is present in the str representation
        self.assertIn("my_city_id", str_place)
        # Test if user_id is present in the str representation
        self.assertIn("my_user_id", str_place)
        # Test if name is present in the str representation
        self.assertIn("My Place", str_place)
        # Test if description is present in the str representation
        self.assertIn("My Description", str_place)

    def test_dictionary_representation(self):
        """Test dictionary representation."""
        # Create a Place instance
        my_place = Place(
            city_id="my_city_id",
            user_id="my_user_id",
            name="My Place",
            description="My Description",
            number_rooms=5,
            number_bathrooms=3,
            max_guest=10,
            price_by_night=100,
            latitude=50.123,
            longitude=-100.321,
            amenity_ids=["amenity_id1", "amenity_id2"]
        )
        # Get dictionary representation
        place_dict = my_place.to_dict()
        # Check if dictionary contains expected key-value pairs
        self.assertEqual(place_dict["city_id"], "my_city_id")
        self.assertEqual(place_dict["user_id"], "my_user_id")
        self.assertEqual(place_dict["name"], "My Place")
        self.assertEqual(place_dict["description"], "My Description")
        self.assertEqual(int(place_dict["number_rooms"]), 5)
        self.assertEqual(int(place_dict["number_bathrooms"]), 3)
        self.assertEqual(int(place_dict["max_guest"]), 10)
        self.assertEqual(int(place_dict["price_by_night"]), 100)
        self.assertEqual(float(place_dict["latitude"]), 50.123)
        self.assertEqual(float(place_dict["longitude"]), -100.321)


if __name__ == "__main__":
    unittest.main()
