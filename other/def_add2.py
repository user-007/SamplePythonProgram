def add(a, b, c):
    print(a, b, c)
    sum = a + b + c
    print(sum)

add(a = 1, c = 3, b = 2)
add(b = 2, c = 3, a = 1)

#Name mismatch error  - Keyword argument
def ctry_details(country, capital)
    print("Capital of", country, "is",capital)

ctry_details(capital = "New Delhi", the_country = "India")
