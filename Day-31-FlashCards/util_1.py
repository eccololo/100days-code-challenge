# with open("./assets/it_words_source_50k.txt", "r") as f_1:
#     data = f_1.readlines()
#
# output_data = []
# for item in data:
#     output_data.append(item.split(" ")[0])
#
# with open("./assets/it_words_50k.txt", "w") as f_2:
#     for word in output_data:
#         text = f"{word}\n"
#         f_2.write(text)

some_list = [["a", "b"], ["c", "d"], ["e", "f"]]
counter = 1
data_set = {}

for row in some_list:
    data_set[counter] = {"question": row[0]}
    data_set[counter] = {"answer": row[1]}
    counter += 1

print(data_set)