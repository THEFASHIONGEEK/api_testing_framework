import unittest
from utils.assertions import assert_status_code, assert_json_value, assert_json_value_in_list

class TestAssertions(unittest.TestCase):
    def test_assert_status_code_pass(self):
        response = MockResponse(status_code=200)
        assert_status_code(response, 200)

    def test_assert_status_code_fail(self):
        response = MockResponse(status_code=404)
        with self.assertRaises(AssertionError) as context:
            assert_status_code(response, 200)
        self.assertIn("Expected status code '200', but got '404'", str(context.exception))

    def test_assert_json_value_pass(self):
        response_json = {"name": "John", "age": 30}
        assert_json_value(response_json, "name", "John")

    def test_assert_json_value_fail(self):
        response_json = {"name": "John", "age": 30}
        with self.assertRaises(AssertionError) as context:
            assert_json_value(response_json, "name", "Jane")
        self.assertIn("Expected value 'Jane' for key 'name', but got 'John'", str(context.exception))

    def test_assert_json_value_in_list_pass(self):
        response_json = {"status": "available"}
        assert_json_value_in_list(response_json, "status", ["available", "pending", "sold"])

    def test_assert_json_value_in_list_fail(self):
        response_json = {"status": "adopted"}
        with self.assertRaises(AssertionError) as context:
            assert_json_value_in_list(response_json, "status", ["available", "pending", "sold"])
        self.assertIn("Expected value not present in '['available', 'pending', 'sold']' for key 'status', but got 'adopted'", str(context.exception))

# Helper class to create a mock response object
class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

if __name__ == "__main__":
    unittest.main()
