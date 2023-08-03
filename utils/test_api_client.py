import unittest
from unittest.mock import patch, MagicMock
from api_client import APIClient

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://example.com"
        self.headers = {"Content-Type": "application/json"}
        self.api_client = APIClient(self.base_url, self.headers)

    def test_get(self):
        endpoint = "test_endpoint"
        params = {"param1": "value1", "param2": "value2"}

        # Mock the requests.get method to return a MagicMock response object
        with patch("requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"message": "Success"}
            mock_get.return_value = mock_response

            response = self.api_client.get(endpoint, params=params)

            # Assert that requests.get was called with the correct arguments
            mock_get.assert_called_once_with(
                f"{self.base_url}/{endpoint}",
                headers=self.headers,
                params=params
            )

            # Assert the response status code and the returned data
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"message": "Success"})

    def test_post(self):
        endpoint = "test_endpoint"
        data = {"key1": "value1", "key2": "value2"}

        # Mock the requests.post method to return a MagicMock response object
        with patch("requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 201
            mock_response.json.return_value = {"message": "Created"}
            mock_post.return_value = mock_response

            response = self.api_client.post(endpoint, data)

            # Assert that requests.post was called with the correct arguments
            mock_post.assert_called_once_with(
                f"{self.base_url}/{endpoint}",
                data='{"key1": "value1", "key2": "value2"}',
                headers=self.headers
            )

            # Assert the response status code and the returned data
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json(), {"message": "Created"})

    def test_put(self):
        endpoint = "test_endpoint"
        data = {"key1": "value1", "key2": "value2"}

        # Mock the requests.put method to return a MagicMock response object
        with patch("requests.put") as mock_put:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"message": "Updated"}
            mock_put.return_value = mock_response

            response = self.api_client.put(endpoint, data)

            # Assert that requests.put was called with the correct arguments
            mock_put.assert_called_once_with(
                f"{self.base_url}/{endpoint}",
                data='{"key1": "value1", "key2": "value2"}',
                headers=self.headers
            )

            # Assert the response status code and the returned data
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"message": "Updated"})

    def test_delete(self):
        endpoint = "test_endpoint"

        # Mock the requests.delete method to return a MagicMock response object
        with patch("requests.delete") as mock_delete:
            mock_response = MagicMock()
            mock_response.status_code = 204  # No Content
            mock_delete.return_value = mock_response

            response = self.api_client.delete(endpoint)

            # Assert that requests.delete was called with the correct arguments
            mock_delete.assert_called_once_with(
                f"{self.base_url}/{endpoint}",
                headers=self.headers
            )

            # Assert the response status code
            self.assertEqual(response.status_code, 204)

if __name__ == "__main__":
    unittest.main()
