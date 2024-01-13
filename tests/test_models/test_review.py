import unittest

from models.review import Review


class TestReview(unittest.TestCase):

    def test_create_review_with_required_attributes(self):
        """test_create_review_with_required_attributes tests that when a"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_create_review_with_all_attributes(self):
        """test_create_review_with_all_attributes tests that when a Review"""
        review = Review(place_id='123', user_id='456', text='test')
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, '123')
        self.assertEqual(review.user_id, '456')
        self.assertEqual(review.text, 'test')

    #  Review instance can be saved successfully
    def test_save_review_successfully(self):
        """test_save_review_successfully tests that when a Review instance is"""
        review = Review()
        review.save()
        self.assertIsNotNone(review.updated_at)

    def test_create_review_with_empty_attributes(self):
        """test_create_review_with_empty_attributes tests that when a"""
        review = Review(place_id='', user_id='', text='')
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_create_review_with_non_string_attributes(self):
        """test_create_review_with_non_string_attributes tests that when a"""
        review = Review(place_id=123, user_id=456, text=789)
        self.assertIsInstance(review, Review)
        self.assertNotEqual(review.place_id, '123')
        self.assertNotEqual(review.user_id, '456')
        self.assertNotEqual(review.text, '789')

    def test_create_review_with_non_existent_attributes(self):
        """test_create_review_with_non_existent_attributes tests that when a"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertFalse(hasattr(review, 'non_existent_attr'))

    def test_create_review_with_invalid_dates(self):
        """test_create_review_with_invalid_dates tests that when a Review"""
        review = Review(created_at='2021-01-01T00:00:00.000000', updated_at='2022-01-01T00:00:00.000000')
        self.assertIsInstance(review, Review)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
