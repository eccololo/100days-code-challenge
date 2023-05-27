a_list = [1, 2, 3]
new_list = [item + 1 for item in a_list]
print(new_list)

name = "Mateusz"
a_name_list = [x_char for x_char in name]
print(a_name_list)

doubled_list = [item * 2 for item in range(1, 5)]
print(doubled_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Freddie", "Eleanor"]

upper_cased_names = [name.upper() for name in names if len(name) > 5]
print(upper_cased_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)