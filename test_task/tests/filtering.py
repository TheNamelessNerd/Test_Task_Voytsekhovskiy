import requests

#Type desired userID
my_userid='8'


#To run the test copy this in Terminal: pytest tests\filtering.py


def test_if_user_id_is_correct():
    assert my_userid in range(1,11)

url = f"https://jsonplaceholder.typicode.com/posts?userId={my_userid}"
my_userid =int(my_userid)

#Expected IDs for this userID
expected_ids = [i for i in range((my_userid-1)*10+1,my_userid*10+1)]

def test_filtering_check_status_code_equals_200():
    response = requests.get(url)
    assert response.status_code == 200


def test_filtering_header_type_equals_json():
    response = requests.get(url)
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['cache-control'] == "max-age=43200"


def test_filtering_id_number_is_correct_and_equals_10():
    response = requests.get(url)
    response_body = response.json()
    assert len(response_body) == 10


def test_filtering_user_id_is_correct():
    response = requests.get(url)
    response_body = response.json()
    for i in response_body:
        assert i["userId"] == my_userid


def test_filtering_associated_ids_are_correct():
    response = requests.get(url)
    response_body = response.json()
    for i in response_body:
        assert i["id"] in expected_ids