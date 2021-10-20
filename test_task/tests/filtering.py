import requests
import pytest
from random import randint

my_userid = randint(1, 10)

# Expected IDs for this userID
expected_ids = [i for i in range((my_userid - 1) * 10 + 1, my_userid * 10 + 1)]


@pytest.fixture()
def url():
    return f"https://jsonplaceholder.typicode.com/posts?userId={my_userid}"


@pytest.fixture()
def res(url):
    response = requests.get(url)
    return response


@pytest.fixture()
def res_body(url):
    response_body = requests.get(url).json()
    return response_body


def test_filtering_user_id_is_appropriate():
    assert my_userid in range(1, 11)


def test_filtering_check_status_code_equals_200(res):
    assert res.status_code == 200


def test_filtering_header_type_equals_json(res):
    assert res.headers['Content-Type'] == "application/json; charset=utf-8"


def test_filtering_id_quantity_is_correct_and_equals_10(res_body):
    assert len(res_body) == 10


def test_filtering_user_id_is_correct(res_body):
    for i in res_body:
        assert i["userId"] == my_userid


def test_filtering_associated_ids_are_correct(res_body):
    for i in res_body:
        assert i["id"] in expected_ids
