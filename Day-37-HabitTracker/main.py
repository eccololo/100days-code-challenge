import requests
import os
from datetime import datetime

USERNAME = "eccololo"
GRAPH_ID = "graph-books-1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# Creating user account on Pixe.la
pixela_api_key = os.environ.get("PIXELA_API_KEY")
pixela_user_parameters = {
    "token": pixela_api_key,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_user_parameters)
# print(response.text)

# Creating a graph on Pixe.la
graph_config = {
    "id": "graph-books-1",
    "name": "Reading Books",
    "unit": "min",
    "type": "int",
    "color": "shibafu",

}

headers = {
    "X-USER-TOKEN": pixela_api_key
}

pixela_graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Posting a value to graph on Pixe.la
pixela_today_date = datetime.now().strftime("%Y%m%d")

pixela_post_value_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
graph_add_value_config = {
    "date": pixela_today_date,
    "quantity": "45"
}

# response = requests.post(url=pixela_post_value_endpoint, json=graph_add_value_config, headers=headers)
# print(response.text)

# Updating a value on pixe.la graph
pixela_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{pixela_today_date}"
graph_update_value_config = {
    "quantity": "15"
}

# response = requests.put(url=pixela_update_endpoint, json=graph_update_value_config, headers=headers)
# print(response.text)

# Delete pixel data in pixe.la

# pixela_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{pixela_today_date}"
# response = requests.delete(url=pixela_delete_endpoint, headers=headers)
# print(response.text)
