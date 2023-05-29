import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {value.letter:value.code for (idx, value) in nato_df.iterrows()}

user_input_list = list(input("Type word you want to spell in nato alphabet: "))
user_input_list_upper = [item.upper() for item in user_input_list]
output_list = [code for (letter, code) in nato_dict.items() if letter.upper() in user_input_list_upper]

# Sort Fix
output_list = [x for _, x in sorted(zip(user_input_list_upper, output_list), key=lambda pair: pair[0])]
print(output_list)
