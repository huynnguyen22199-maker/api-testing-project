import requests

def test_bi_loi():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    assert response.status_code == 999
    assert response.json()["name"] == "Ten sai"