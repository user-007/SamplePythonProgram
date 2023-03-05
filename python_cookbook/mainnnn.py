ls1 = [5, 10, 25, 20, 15]
ls1[0], ls1[1], ls1[3], ls1[4] = ls1[4], ls1[3] = ls1[4]
print(ls1)

ls = [5,10, 25, 20, 15, 24, 32]
length = len(ls)

for i in range(length//2):
    ls[i], ls[length - i - 1] = ls[length - i -1], ls[i]

print(ls)

lst = [0, 1, 2, 3, 4]
new_list = [ls]