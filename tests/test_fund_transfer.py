import requests

BASE_URL = "http://localhost:8080"

def test_fund_transfer():
    payload = {
        "fromAccount": "ACC12345",
        "toAccount": "ACC67890",
        "amount": 5000
    }

    response = requests.post(f"{BASE_URL}/api/v1/transfer", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["status"] == "SUCCESS"
