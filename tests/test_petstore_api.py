import csv
import os
import logging

import pytest

from utils.api_client import APIClient
from utils.assertions import assert_status_code, assert_json_value, assert_json_value_in_list


@pytest.fixture
def api_client():
    base_url = "https://petstore.swagger.io/v2"
    headers = {"Content-Type": "application/json"}
    return APIClient(base_url, headers=headers)


def read_users_data_from_csv():
    users_data = []
    csv_file_path = os.path.join(os.path.dirname(__file__), "data/users_data.csv")
    with open(csv_file_path, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            users_data.append(row)
    return users_data


def test_create_users_with_array(api_client):
    print("test create users")
    users_data = read_users_data_from_csv()
    response = api_client.post("user/createWithArray", data=users_data)
    assert_status_code(response, 200)


def test_update_user(api_client):
    username = "user1"
    updated_user_data = {
        "id": 1,
        "username": "updated_user1",
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "password": "new_password123",
        "phone": "111-222-3333",
        "userStatus": 1
    }
    response = api_client.put(f"user/{username}", data=updated_user_data)
    assert_status_code(response, 200)

def test_get_user_by_updated_username(api_client):
    updated_username = "updated_user1"
    response = api_client.get(f"user/{updated_username}")
    assert_status_code(response, 200)
    assert_json_value(response.json(), "username", updated_username)


def test_create_pets(api_client):
    pet_data = {
        "id": 1,
        "category": {
            "id": 1,
            "name": "Dog"
        },
        "name": "Doggie",
        "photoUrls": [
            "https://example.com/doggie.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "pettag"
            }
        ],
        "status": "available"
    }
    response = api_client.post("pet", pet_data)
    assert_status_code(response, 200)


def test_update_pet(api_client):
    pet_id = 1
    updated_pet_data = {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": "Dog"
        },
        "name": "Doggie",
        "photoUrls": [
            "https://example.com/doggie.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "pettag"
            }
        ],
        "status": "sold"
    }
    response = api_client.put("pet", updated_pet_data)
    assert_status_code(response, 200)


def test_get_pet_by_status(api_client):
    params = {"status": "available", "status": "pending", "status": "sold"}
    response = api_client.get(f"pet/findByStatus", params)
    assert_status_code(response, 200)
    pet_list = response.json()
    for pet in pet_list:
        assert_json_value_in_list(pet, "status", ["available", "pending", "sold"])
