import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
import requests

API_URL = "https://zfnm62l55ess2bf7nmifbfcp5i0nzcjk.lambda-url.eu-north-1.on.aws/"

def test_api_returns_expected_response():
    response = requests.get(API_URL)
    assert response.status_code == 200
    data = response.json()
    assert 'views' in data
    assert isinstance(data['views'], int)

def test_api_updates_database():
    initial_response = requests.get(API_URL)
    initial_views = initial_response.json()['views']

    # Make another request to increment the views
    updated_response = requests.get(API_URL)
    updated_views = updated_response.json()['views']

    assert updated_views == initial_views + 1

def test_api_handles_unexpected_input():
    # Test with an unexpected HTTP method (POST)
    response = requests.post(API_URL, json={"invalid": "input"})
    assert response.status_code == 200  # Method Not Allowed

    # Test with an invalid URL
    invalid_url = API_URL + "/invalid"
    response = requests.get(invalid_url)
    assert response.status_code == 404  # Not Found

def test_api_edge_cases():
    # Test with an uninitialized visitor count
    # This would require resetting the database or mocking the Lambda function
    pass

if __name__ == "__main__":
    pytest.main()
