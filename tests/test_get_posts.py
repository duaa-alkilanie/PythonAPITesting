import json
import sys
import random
import jsonpath
import pytest
import requests

from JSONPlaceholder.tests import end_points

# defined url,path for posts,header to send with GET request
url = end_points["url"]


@pytest.mark.GET
@pytest.mark.happyScenario
# get the first post_id and verify  is not return empty
def test_get_first_post_id():
    path = "/posts"
    header = {"Content-Type": "application/json"}
    response = requests.get(url=url + path, headers=header)
    response_text = json.loads(response.text)
    print("response ==", response_text)
    user_id = jsonpath.jsonpath(response_text[0], "userId")
    print(user_id)
    assert response.status_code == 200
    assert user_id is not None ,"This user id has empty value or false value"


@pytest.mark.GET
@pytest.mark.happyScenario
# get post id randomly
def test_post_id_randomly():
    path = "/posts"
    header = path = "/posts"
    header = {"Content-Type": "application/json", "charset": "UTF-8"}
    response = requests.get(url=url + path, headers=header)
    response_text = json.loads(response.text)
    print("response ==", response_text)
    user_id_for_posts = [i["userId"] for i in response_text]
    print(user_id_for_posts)
    print("random-id==", random.choice(user_id_for_posts))
    assert response.status_code == 200
    assert user_id_for_posts is not None ,"This user id has empty value or false value"



@pytest.mark.GET
@pytest.mark.happyScenario
# Using any userID, get this user’s associated album title and verify -->
# that the album title does not exceed 300 characters
def test_any_user_id_and_verify_the_album_title_does_not_exceed_300_characters():
    max_size = 100
    path = "/users/1/albums"
    header = {"Content-type": "application/json",
              "charset": "UTF-8"}
    response = requests.get(url=url + path, headers=header)
    response_text = json.loads(response.text)
    print("response_text==", response_text)
    the_albums_title = jsonpath.jsonpath(response_text[0], "title")
    print("the_albums_title==", the_albums_title)
    size = sys.getsizeof(the_albums_title)
    print("size of album title == ", size)

    assert size <= max_size,"this message if size >= max_size"
    return the_albums_title


@pytest.mark.GET
@pytest.mark.happyScenario
# For a specific (userId) print all (titles) in (todos) where “completed” =false

def test_for_specific_user_id_print_all_titles_where_completed_with_false():
    path = "/users/1/todos?completed=false"
    header = {"Content-type": "application/json"
              }

    response = requests.get(url=url + path, headers=header)
    response_text = json.loads(response.text)
    print("response_text==", response_text)
    all_titles_for_todos_with_completed_false = [i["title"] for i in response_text]
    print(all_titles_for_todos_with_completed_false)
    print("status_code==", response.status_code)
    assert response.status_code == 200
    assert all_titles_for_todos_with_completed_false is not None ,\
        "This all_titles_for_todos_with_completed_false  has empty value or false value"

