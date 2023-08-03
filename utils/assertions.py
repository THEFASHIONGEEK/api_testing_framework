def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"

def assert_json_value(response_json, key, expected_value):
    assert key in response_json, f"Key '{key}' not found in the response JSON"
    assert response_json[key] == expected_value, f"Expected value {expected_value} for key {key}, but got {response_json[key]}"

def assert_json_value_in_list(response_json, key, expected_value_list):
    assert key in response_json, f"Key '{key}' not found in the response JSON"
    assert response_json[key] in expected_value_list, f"Expected value not present in {expected_value_list} for key {key}, but got {response_json[key]}"

