import requests


# To run the test copy this in Terminal: pytest tests\get_by_id.py


def test_get():
    # Here we iterate only 11 times, since we have a repeating pattern in data (1 user, 10 posts)
    # So we don't need to check all the data, since the list could be expanded, and testing all data
    # would take unreasonable amount of time without necessity
    for id in range(1,12):

        # Computing expected UserId

        if id % 10 == 0:
            my_user_id =id // 10
        else:
            my_user_id = (id + 10) // 10

        # Initiating GET request

        response = requests.get( f"https://jsonplaceholder.typicode.com/posts/{id}")
        response_body = response.json()

        # Asserting that information is correct

        assert response.status_code == 200  # Check status code

        assert response.headers['Content-Type'] == "application/json; charset=utf-8" # Check that body is correct

        assert response_body["id"] == id  # Check that ID in the body matches the query ID

        assert response_body["userId"] == my_user_id # Check that response has correct UserId for given query ID
