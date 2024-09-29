import unittest
import requests
from datetime import datetime
class TestReviewAPI(unittest.TestCase):

    base_url = 'http://54.83.149.21:8002/reviews'
    local = 0
    if local:
        base_url = 'http://localhost:8000/reviews'
    else:
        base_url = 'http://54.83.149.21:8002/reviews'
    review_id = ''
    user_id = 'uuid-user-1234'
    target_id = 'uuid-product-5678'

    def test_1_create_review(self):
        url = f"{self.base_url}/reviews"
        data = {
            "user_id": self.user_id,
            "review_type": "PRODUCT",
            "target_id": self.target_id,
            "rating": 5,
            "content": "Great product!",
            "extra": {"color": "red", "size": "M"}
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.__class__.review_id = json_response.get("review_id")
        self.assertIsNotNone(self.review_id)

    def test_2_get_review(self):
        url = f"{self.base_url}/reviews/{self.review_id}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['user_id'], self.user_id)

    def test_3_update_review(self):
        url = f"{self.base_url}/reviews/{self.review_id}"
        data = {
            "rating": 4,
            "content": "Actually, it's good but has some issues.",
            "status": "approved",
            "extra": {"color": "red", "size": "M", "warranty": "1 year"}
        }
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['status'], 'Review updated successfully')

    def test_4_get_updated_review(self):
        url = f"{self.base_url}/reviews/{self.review_id}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['rating'], 4)
        self.assertEqual(json_response['status'], 'approved')

    def test_5_delete_review(self):
        url = f"{self.base_url}/reviews/{self.review_id}"
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['status'], 'Review deleted successfully')

    def test_6_get_deleted_review(self):
        url = f"{self.base_url}/reviews/{self.review_id}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 404)
    def test_7_search_reviews(self):
        url = f"{self.base_url}/reviews/search"
        data = {
            "user_id": self.user_id,
            "target_id": self.target_id,
            "review_type": "product",
            "status": "approved"
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        print(json_response)
        self.assertTrue(len(json_response) >= 1)
        review = json_response[0]
        self.assertEqual(review['user_id'], self.user_id)
        self.assertEqual(review['target_id'], self.target_id)
        self.assertEqual(review['review_type'], 'product')
        self.assertEqual(review['status'], 'approved')

if __name__ == '__main__':
    unittest.main()