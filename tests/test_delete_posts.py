import json

import jsonpath
import pytest
import requests

from JSONPlaceholder.tests import end_points
from JSONPlaceholder.tests.test_create_posts import create_a_new_posts

# defined url,path for posts,header to send with GET request
url = end_points["url"]


@pytest.mark.Delete
@pytest.mark.happyScenario
# post using same userID with a non-empty title and body,verify the correct response to be 201
def test_delete_a_new_post():
    user_id, id = create_a_new_posts()
    path = "/posts/" + str(user_id)
    print(user_id, id)
    header = {"Content-Type": "application/json", "charset": "UTF-8"}
    response = requests.delete(url=url + path)
    response_text = json.loads(response.text)
    print("response==", response_text)
    assert len(response_text) == 0, "the list is non empty"
    print("the list is non empty")
    assert response.status_code == 200
    print("status_code==", response.status_code)
