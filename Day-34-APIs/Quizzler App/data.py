import requests


def get_questions():
    # Write your code here.
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    data = response.json()
    questions_list = data["results"]
    return questions_list


question_data = get_questions()