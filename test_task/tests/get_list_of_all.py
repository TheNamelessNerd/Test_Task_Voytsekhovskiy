import requests

#To run the test copy this in Terminal: pytest tests\get_list_of_all.py



url = "https://jsonplaceholder.typicode.com/posts/"


def test_getall_check_status_code_equals_200():
    response = requests.get(url)
    assert response.status_code == 200


def test_getall_header_type_equals_json():
    response = requests.get(url)
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    assert response.headers['Connection'] == "keep-alive"
    assert response.headers['cache-control'] == "max-age=43200"


def test_get_all_id_number_is_correct_and_equals_100():
    response = requests.get(url)
    response_body = response.json()
    assert len(response_body) == 100


def test_get_all_user_id_is_correct():
    response = requests.get(url)
    response_body = response.json()

    for id in response_body:
        if id % 10 == 0:
            my_user_id = id // 10
        else:
            my_user_id = (id + 10) // 10
        assert id["userId"] == my_user_id


def test_filtering_associated_ids_are_correct():
    response = requests.get(url)
    response_body = response.json()
    for i in range(1,101) in response_body:
        assert i["id"] == i