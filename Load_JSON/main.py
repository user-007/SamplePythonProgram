# with open("a_file.txt") as file:
#     file.read()

# a_dictionary = {"key":"value"}
# value = a.dictionary["noon_existing_key"]

#  fruit_list = ["Apple", "Banana", "pear"]
# fruit = fruit_list[3]

# if something fails =>..
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdsdaadfs"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("This is an eror that I made up")
    # file.close()
    # print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human hights should not be .....")
bmi = weight/height ** 2
print(bmi)
