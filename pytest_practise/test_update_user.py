import requests
import pytest
#@pytest.fixture
def update1_user():
    url = "https://reqres.in/api/users/2"
    data = {
        "name": "Paulo Updated"
    }
    response = requests.put(url, data=data)
    return 5

   
# @pytest.mark.demo
"""def test_demo(update1_user):
    url = "https://reqres.in/api/users/2"
    print(update1_user)
    data = {
        "name": "Paulo Updated"
    }
    response = requests.put(url, data=data)
    assert update1_user == 15
"""

@pytest.mark.parametrize("a","b","output",[(2,3,5)])
def test_update3_user(a,b,output):
    if output==a+b:
        assert True
    url = "https://reqres.in/api/users/2"
    data = {
        "name": "Paulo Updated"
    }
    response = requests.put(url, data=data)
    assert response.status_code == 200