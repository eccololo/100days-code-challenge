import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
accepted = False
while not accepted:
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter from english alphabet are valid input.")
        word = input("Enter a word: ").upper()
    else:
        accepted = True

print(output_list)
