import requests
import random


# k is the size of random test pool of IDs, set to 100 to test all, or set my_ids to desired list of IDs
k = 10

ids = range(1, 101)
my_ids = random.sample(ids, k)


def test_get_by_id():
    for id_k in my_ids:
        # Computing expected UserId

        if id_k % 10 == 0:
            my_user_id = id_k // 10
        else:
            my_user_id = (id_k + 10) // 10

        # Initiating GET request for current ID

        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_k}")
        response_body = response.json()

        # Asserting that information is correct

        assert response.status_code == 200  # Check status code

        assert response.headers['Content-Type'] == "application/json; charset=utf-8"  # Check that header is correct

        assert response_body["id"] == id_k  # Check that ID in the response matches the query ID

        assert response_body["userId"] == my_user_id  # Check that response has correct UserId for given query ID
