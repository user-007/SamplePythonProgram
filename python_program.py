str = input("Enter a string: ")
c = 0
ch = 0

for i in str:
    if i == " ":
        if ch!=0:
            c = c + 1
        ch = 0
    else:
        ch = ch +1

    if ch!=0:
        c = c +1
    print(c)