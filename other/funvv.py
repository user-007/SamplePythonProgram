def sq_sum(ls):
    pass
    sum = 0
    for number in ls:
        sq = number ** 2
        sum  = sq+sum
    print(sum)

l1 = [10, 2, 4, 5, 4, 2]
l2 = [1, 4, 6, 7, 8, 9]

sq_sum(l1)
sq_sum(l2)

#print(ls) #Produces an error as .....