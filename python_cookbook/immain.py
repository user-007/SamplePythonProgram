ls1 = [1, 2, 3]
ls2 = ls1[:]
ls1[1] = 4
print(ls1)
print(ls2)
print(id(ls1))
print(id(ls2))