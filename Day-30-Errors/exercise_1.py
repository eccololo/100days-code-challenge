# FileNotFound Exception
# KeyError Exception
try:
    file = open("some_file.txt")
    some_dict = {"key": "message"}
    # print(some_dict["key2"])
except FileNotFoundError:
    file = open("some_file.txt", "w")
    file.write("Something")
except KeyError as err_msg:
    print(f"The key {err_msg} does not exists.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("The file was closed.")
