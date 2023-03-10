#The try block will generate a NameError, because x is not defined:
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["asdfasdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} down no exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")