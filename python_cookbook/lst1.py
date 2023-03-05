ls1 = [5, 10, 25, 20, 15]
ls2 = ['A', 'B', 'C']
print('List1 before:',ls1)
print('List2 before:', ls2)
#a, b = b, a
ls2,ls1 = ls1, ls2
print('List1 before:',ls1)
print('List2 before:', ls2)
total = 0
for element in ls:
    total +=element

