def func(list_2):
    print("A:", list_2)
    print("B:", list_1)
    del list_2[1] #change list_2 & list_1 also, OP, [1, 3, 4]
    del list_1[2] #change list_1 & list_2 also, OP, [1, 3]