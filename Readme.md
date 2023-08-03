# API Testing Framework

This is a simple and scalable API testing framework designed to validate REST APIs using Python. The framework uses FastAPI as the web framework for creating APIs and provides a test suite to validate various API calls and responses.

## Getting Started

To use this framework, follow the steps below:

1. Install Python 3.6 or later on your system.

2. Clone this repository to your local machine:
   ```
   git clone https://github.com/THEFASHIONGEEK/api_testing_framework.git
   cd api-testing-framework
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Tests

To execute the test cases, use the pytest framework. You can run the tests by executing the following command from the root directory of the project:

```
pytest tests -v --html=reports/report.html
```

This will run all the test cases and generate an HTML report in the `reports` directory. The `-v` flag enables verbose mode to display detailed test results.

## Test Cases

The test cases are located in the `tests` directory, organized based on different functionalities. Each test case performs an API call and validates the response using custom assertions. The test cases cover the following API calls:

- Create multiple users with an array
- Update a user's username and other details
- Get user by the updated username
- Create multiple pets
- Update pet's status and other details
- Get pets by status and verify the updated status of pets

## API Client

The `utils/api_client.py` module provides the `APIClient` class, which is used to make API requests. The class handles GET, POST, PUT, and DELETE requests and provides methods to interact with the APIs. It also supports setting custom headers and handling responses.

## Custom Assertions

The `utils/assertions.py` module contains custom assertion functions that are used to validate API responses. These assertions provide informative error messages to aid in quick identification of issues during testing.

## Extensibility

The framework follows a modular design to promote reusability and maintainability. It can be easily extended by adding new test cases, custom assertions, or utility functions. You can also integrate it with other third-party libraries to enhance its capabilities.

## Improvements and Contributions

This framework is a starting point for API testing and can be further enhanced by adding more features, better reporting, performance testing, and handling edge cases. Contributions and feedback are welcome to make the framework more robust and effective.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

For any questions or feedback, feel free to contact us at ahemanth14@gmail.com.

Happy Testing!