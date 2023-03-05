def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n-=1
    print('Done!')
