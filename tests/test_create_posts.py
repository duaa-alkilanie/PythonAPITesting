import json
import pytest
import jsonpath
import requests

from JSONPlaceholder.tests import end_points

# defined url,path for posts,header to send with GET request
url = end_points["url"]


# post using same userID with a non-empty title and body,verify the correct response to be 201
def create_a_new_posts():
    path = "/posts"
    header = {"Content-Type": "application/json", "charset": "UTF-8"}
    body = {
        "title": "duaa alkilanii",
        "body": "body fro new posts",
        "userId": 1
    }
    response = requests.post(url=url + path, headers=header, json=body)
    response_text = json.loads(response.text)
    print("response==", response_text)
    print(response.status_code)
    user_id = jsonpath.jsonpath(response_text, "userId")
    id = jsonpath.jsonpath(response_text, "id")
    print("user_id==", user_id)
    print("id==", id)
    assert response.status_code == 201
    return user_id[0], id[0]


@pytest.mark.TopPriority
@pytest.mark.happyScenario
def test_create_a_new_posts_for_same_user():
    user_id = create_a_new_posts()
    assert user_id[0] == 1, "this message when user id is != the user id which create with"
