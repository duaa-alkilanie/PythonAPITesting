import json
import jsonpath
import pytest
import requests

from JSONPlaceholder.tests import end_points
from JSONPlaceholder.tests.test_create_posts import create_a_new_posts

# defined url,path for posts,header to send with GET request
url = end_points["url"]


@pytest.mark.UPDATE
@pytest.mark.happyScenario
# test updated post_id was created before
def test_updated_for_a_new_post_was_added():
    user, id = create_a_new_posts()
    print(user, id)
    path = "/posts/" + str(user)
    print(path)
    header = {"Content-Type": "application/json", "charset": "UTF-8"}
    body = {
        "title": "duaa alkilani QA Engineer ",
        "userId": user,
        "id": id
    }
    response = requests.put(url=url + path, headers=header, json=body)
    response_text = json.loads(response.text)
    print("response==", response_text)
    print(response.status_code)
    # user_id = jsonpath.jsonpath(response_text,["userId"])
    id_after_updated = jsonpath.jsonpath(response_text, "id")
    # print("user_id==", user_id,"id==",id)
    assert response.status_code == 200
    # assert id was change after updated user_id
    assert id != user,"this message when id is the same off user id "

    print("user_id_who_will_updated==", user)
