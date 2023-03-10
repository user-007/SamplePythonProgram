def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(1, 2)


def test(*args):
    print(args)


test(1, 2, 3, 5)
pri