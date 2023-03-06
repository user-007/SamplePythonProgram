vowels = 0
consonants = 0

for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels + l
    elif letter == "":
        pass
    else:
        consonants = consonants + l

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))


