def modify(ls):
    del ls[2]
    print("Inside list value:", ls)


l = [10, 2, 4, 5, 4, 2]

print("1. List", l)
modify(l)
print("2.List", l)
