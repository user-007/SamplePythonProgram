PLACEHOLDER  = "{name}"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open("./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        print(new_letter)
