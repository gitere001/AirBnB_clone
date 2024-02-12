#!/usr/bin/python3
"""
test model for class User
"""
import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    class for testing class User
    """
    def setUp(self):
        # creating a temporary file to save
        self.my_test_file = "my_test_file.json"
        models.storage.__file_path = self.my_test_file
        models.storage.save()

    def tearDown(self):
        # remove previously created file after use
        if os.path.exists(self.my_test_file):
            os.remove(self.my_test_file)

    def test_user_attributes(self):
        # creating a new user instance
        my_user = User()
        # check if attribute 'email' is an empty string
        self.assertEqual(my_user.email, "")
        # check if attribute 'password' is an empty string
        self.assertEqual(my_user.password, "")
        # check if attribute 'first_name' is an empty string
        self.assertEqual(my_user.first_name, "")
        # check if attribute 'last_name' is an empty string
        self.assertEqual(my_user.last_name, "")

    def test_User_inheritance_from_base_class(self):
        # creating a new user instance
        my_user = User()
        # testing is User class is a subclass of BaseModel class
        self.assertEqual(issubclass(User, BaseModel), True)
        # Additional assertion to check if my_user is an instance of BaseModel
        self.assertIsInstance(my_user, User)

    def test_user_str_representation(self):
        # creating a new user instance
        my_user = User()
        # setting attributes of User instance
        my_user.email = "jamesgitere@example.com"
        my_user.first_name = "James"
        my_user.last_name = "Gitere"
        my_user.password = "Password123"
        # getting str representation of User instance
        str_user = str(my_user)
        # test if "user" is present in the str representation
        self.assertIn("User", str_user)
        # test if email is present in the str representation
        self.assertIn("jamesgitere@example.com", str_user)
        # test if first_name is present in the str representation
        self.assertIn("James", str_user)
        # test if last_name is present in the str representation
        self.assertIn("Gitere", str_user)

    def test_user_to_dict(self):
        # creating a new user instance
        my_user = User()
        # setting attributes of User instance
        my_user.email = "jamesgitere@example.com"
        my_user.first_name = "James"
        my_user.last_name = "Gitere"
        my_user.save()
        # getting dict representation of User instance
        user_dict = my_user.to_dict()
        # checking if 'email' key in dict matches the value
        self.assertEqual(user_dict['email'], "jamesgitere@example.com")
        # checking if 'first_name' key in dict matches the value
        self.assertEqual(user_dict['first_name'], "James")
        # checking if 'last_name' key in dict matches the value
        self.assertEqual(user_dict['last_name'], "Gitere")

    def test_user_instance_creation(self):
        # creating an new object with arguments
        my_user = User(email="Jamesgitere@example.com",
                       password="Password123",
                       first_name="James",
                       last_name="Gitere")
        # check if the 'email' attribute is set correctly
        self.assertEqual(my_user.email, "Jamesgitere@example.com")
        # check if the 'password' attribute is set correctly
        self.assertEqual(my_user.password, "Password123")
        # check if the 'first_name' attribute is set correctly
        self.assertEqual(my_user.first_name, "James")
        # check if the 'last_name' attribute is set correctly
        self.assertEqual(my_user.last_name, "Gitere")

    def test_user_instance_to_dict(self):
        # creating an new object with attributes
        my_user = User(email="Jamesgitere@example.com",
                       password="Password123",
                       first_name="James",
                       last_name="Gitere")
        # converting my_user to dict
        my_user_dict = my_user.to_dict()
        # checking if 'email' is reprentented correctly
        self.assertEqual(my_user_dict['email'], "Jamesgitere@example.com")
        # checking if 'password' is reprentented correctly
        self.assertEqual(my_user_dict['password'], "Password123")
        # checking if 'first_name' is reprentented correctly
        self.assertEqual(my_user_dict['first_name'], "James")
        # checking if 'last_name' is reprentented correctly
        self.assertEqual(my_user_dict['last_name'], "Gitere")

    def test_user_id_generation_uniqueness(self):
        # creating 2 different instances
        user1 = User()
        user2 = User()
        # checking if the 2 'id' attributes are unique
        self.assertNotEqual(user1.id, user2.id)


if __name__ == "__main__":
    unittest.main()
