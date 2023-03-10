numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
name = "Angela"
letter_list = [letter for letter in name]
range_list = [num*2 for num in range(1, 5)]
names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
print(names)

short_names = [name for n in names if len(name) < 5]

long_names = [name.upper() for name in names if len(name) > 5]
