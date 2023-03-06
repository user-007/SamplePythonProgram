films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}
while True:
    choice = input("What film would you like to watch?:").strip().title()

    if choice in films:
        age = int(input("How old are you").strip())
    #check user age
        if age >= films[choice]:
            print("Enjoy the film")
        else:
            print("You are too young to watch this film")
    else:
        print("We don't have that film")