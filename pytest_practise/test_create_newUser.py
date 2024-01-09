import requests
def test_create_new_user():
    url = "https://reqres.in/api/users"
    data = {
        "name": "Paulo Oliveira",
        "movies": ["I Love You Man", "Role Models"]
    }
    response = requests.post(url, data=data)
    assert response.status_code == 201