import json
import logging

import requests


class APIClient:
    def __init__(self, base_url,headers):
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        logging.info(f"Get {url} - Response {response.status_code}")
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        logging.info(f"Get {url} - Response {response.status_code}")
        return response


    def put(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        logging.info(f"Get {url} - Response {response.status_code}")
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, headers=self.headers)
        logging.info(f"Get {url} - Response {response.status_code}")
        return response

