with open("./assets/it_words_source_50k.txt", "r") as f_1:
    data = f_1.readlines()

output_data = []
for item in data:
    output_data.append(item.split(" ")[0])

with open("./assets/it_words_50k.txt", "w") as f_2:
    for word in output_data:
        text = f"{word}\n"
        f_2.write(text)
