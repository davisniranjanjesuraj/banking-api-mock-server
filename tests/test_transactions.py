import requests

BASE_URL = "http://localhost:8080"

def test_transaction_history():
    response = requests.get(f"{BASE_URL}/api/v1/account/transactions")
    assert response.status_code == 200

    data = response.json()
    assert len(data["transactions"]) >= 1
