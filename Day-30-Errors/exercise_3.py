data_dict = [
    {"Likes": 15, "Comments": 5},
    {"Likes": 2, "Comments": 3},
    {"Comments": 6}
]

total_likes = 0

for post_data in data_dict:
    try:
        total_likes = total_likes + post_data["Likes"]
    except KeyError:
        pass

print(total_likes)