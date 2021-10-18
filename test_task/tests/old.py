import requests

#Type desired ID
my_id=11

#Computing expected UserId
if my_id % 10 == 0:
    my_user_id = my_id//10
else: my_user_id = (my_id+10)//10


#To run the test copy this in Terminal: pytest tests\



url = f"https://jsonplaceholder.typicode.com/posts/{my_id}"


def test_get_check_status_code_equals_200():
    response = requests.get(url)
    assert response.status_code == 200


def test_get_header_type_equals_json():
    response = requests.get(url)
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"


def test_get_id_is_correct():
    response = requests.get(url)
    response_body = response.json()
    assert response_body["id"] == my_id


def test_get_user_id__is_correct():
    response = requests.get(url)
    response_body = response.json()
    assert response_body["userId"] == my_user_id
