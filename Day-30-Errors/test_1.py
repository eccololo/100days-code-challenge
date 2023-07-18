import json

# data =  [{'amazon.com': {'login': 'mateusz@gmail.com', 'password': '58Ia3P(Zfx1)Z))a'}}]
# item0 = {'amazon.com': {'login': 'mateusz@gmail.com', 'password': '58Ia3P(Zfx1)Z))a'}}

# data = [{'udemy.com': {'login': 'mateusz@gmail.com', 'password': '0x4oXDBM%ay%0np#'}}, {'amazon.com': {'login': 'mateusz@gmail.com', 'password': '58Ia3P(Zfx1)Z))a'}}]
# item0 = {'udemy.com': {'login': 'mateusz@gmail.com', 'password': '0x4oXDBM%ay%0np#'}}
# item1 = {'amazon.com': {'login': 'mateusz@gmail.com', 'password': '58Ia3P(Zfx1)Z))a'}}

www = "udemy.com"
login = "mateusz@gmail.com"

with open("test_1.json") as f:
    data = json.load(f)

# for item in data:
#     data_www = list(item.keys())[0]
#     data_login = item[www]['login']
#     if www in data_www and login in data_login:
#         print("loop")

print(data)
