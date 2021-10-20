import requests
import pytest


@pytest.fixture()
def url():
    return "https://jsonplaceholder.typicode.com/posts/"


@pytest.fixture()
def res(url):
    response = requests.get(url)
    return response


@pytest.fixture()
def res_body(url):
    response_body = requests.get(url).json()
    return response_body


def test_get_all_check_status_code_equals_200(res):
    assert res.status_code == 200


def test_get_all_header_type_equals_json(res):
    assert res.headers['Content-Type'] == "application/json; charset=utf-8"


def test_get_all_id_quantity_is_correct_and_equals_100(res_body):
    assert len(res_body) == 100


def test_get_all_user_ids_are_correct(res_body):
    for user in res_body:
        assert user["userId"] in range(1,11)


def test_get_all_ids_are_correct(res_body):
    for i, id_k in (enumerate(res_body, 1)):
        assert id_k["id"] == i
