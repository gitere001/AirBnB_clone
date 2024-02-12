import os
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

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
        # Create a Review instance
        my_review = Review()
        # Check if attributes are initialized correctly
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")

    def test_inheritance_from_base_model(self):
        """Test inheritance from BaseModel."""
        # Create a Review instance
        my_review = Review()
        # Check if Review class inherits from BaseModel
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(my_review, Review)

    def test_string_representation(self):
        """Test string representation."""
        # Create a Review instance
        my_review = Review(
            place_id="123",
            user_id="456",
            text="Great experience!"
        )
        str_my_review = str(my_review)
        # Test if "123" is present in the str representation
        self.assertIn("123", str_my_review)
        # Test if "456" is present in the str representation
        self.assertIn("456", str_my_review)
        # Test if "Great experience!" is present in the str representation
        self.assertIn("Great experience!", str_my_review)

    def test_dictionary_representation(self):
        """Test dictionary representation."""
        # Create a Review instance
        my_review = Review()
        # Set attributes
        my_review.place_id = "123"
        my_review.user_id = "456"
        my_review.text = "Great experience!"
        # Get dictionary representation
        review_dict = my_review.to_dict()
        # Check if dictionary contains expected key-value pairs
        self.assertEqual(review_dict["place_id"], "123")
        self.assertEqual(review_dict["user_id"], "456")
        self.assertEqual(review_dict["text"], "Great experience!")

    def test_instance_creation_with_arguments(self):
        """Test instance creation with arguments."""
        # Create a Review instance with arguments
        my_review = Review(place_id="123", user_id="456",
                           text="Great experience!")
        # Check if attributes are set correctly
        self.assertEqual(my_review.place_id, "123")
        self.assertEqual(my_review.user_id, "456")
        self.assertEqual(my_review.text, "Great experience!")

    def test_instance_creation_with_dictionary(self):
        """Test instance creation with dictionary."""
        # Create a dictionary
        review_dict = {
            "id": "789",
            "place_id": "123",
            "user_id": "456",
            "text": "Great experience!",
            "__class__": "Review",
        }
        # Create a Review instance from the dictionary
        my_review = Review(**review_dict)
        # Check if attributes are set correctly
        self.assertEqual(my_review.id, "789")
        self.assertEqual(my_review.place_id, "123")
        self.assertEqual(my_review.user_id, "456")
        self.assertEqual(my_review.text, "Great experience!")


if __name__ == "__main__":
    unittest.main()
