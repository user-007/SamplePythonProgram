from itertools import chain

list_1 = ["A","B","C"]
list_2 = [1,2,3]


# chain 2 lists
for i in chain(list_1, list_2):
    print(i)
