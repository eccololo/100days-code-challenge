with open("2.1_file.txt", "r") as f:
    data_1 = f.readlines()
    data_1 = [item.replace("\n", "") for item in data_1]

with open("2.2_file.txt", "r") as f:
    data_2 = f.readlines()
    data_2 = [item.replace("\n", "") for item in data_2]

output = [int(item) for item in data_1 if item in data_2]

print(output)