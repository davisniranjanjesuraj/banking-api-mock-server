import requests

BASE_URL = "http://localhost:8080"

def test_account_balance():
    response = requests.get(f"{BASE_URL}/api/v1/account/balance")
    assert response.status_code == 200

    data = response.json()
    assert data["accountId"] == "ACC12345"
    assert data["balance"] > 0
