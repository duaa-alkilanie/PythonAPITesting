
* Pre-requistes

# Install Python 3 , V.3.8
# Install PyCharm or any other preferred python editor

* Running test-suite

# Create virtual env. using below command
> ubuntu: python -m venv venv

# show all plugin:
>> python -m pip list

# Running pytest :
>> python -m pytest

# (Install test-suite dependencies using below command)

>> pip install -r requirements.txt

#Running pytest by using Grouping test case by tags 
 >>pytest -s -v  -m Delete tests
 >> pytest -s -v  -m TopPriority tests
 >>pytest -s -v  -m "not TopPriority" tests
 >>pytest -s -v  -m GET tests
 >>pytest -s -v  -m UPDATE tests 
 
#Running two testCases with two tags 
 >> pytest -s -v  -m "GET and  happyScenario"  tests
 
#Running two testCases with one of two tags
>>pytest -s -v  -m "GET or Delete "  tests

#Disbale warnings
>>pytest -s -v --disable-pytest-warnings -m GET   tests
or
>> add pytest-ini_file 

#to generate report.xml
> install  pipenv install pytest-xml   
> run % pipenv run python -m pytest -v --junitxml="JSONPlaceholder.xml"
#to generate report.html
> pip install pytest-html
>> Run the command :
>pytest --html=report.html.

=========================================================
**# test cases  for GET Method :**

# get the first post_id and verify  is not return empty
>>test_get_first_post_id

# Using any userID, get this user’s associated album title and verify that the album title does not exceed 300 characters
>>test_any_user_id_and_verify_the_album_title_does_not_exceed_300_characters
# get post id randomly
>>test_post_id_randomly
#For a specific (userId) print all (titles) in (todos) where “completed” =false
>>test_for_specific_user_id_print_all_titles_where_completed_with_false


**# test cases for UPDATE Method :**
#test updated post_id was created before
>>test_updated_for_a_new_post_was_added


**# test case for CREATE Method:**
# post using same userID with a non-empty title and body,verify the correct response to be 201
>>test_create_a_new_posts


