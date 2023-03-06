print("abc")
print(*"abc")

print("a", "b", "c")


def add(x, y):
    return x + y


def add(x, y):
    return x + y


def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return (total)

add(1,2,3,4,5,6,7,8,9)