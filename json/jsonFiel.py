# json.dump()
# json.load()
# json.update()
import json

# Opening JSON file
with open('jsonF.py') as json_file:
    data = json.load(json_file)

    # Print the type of data variable
    print("Type:", type(data))

    # Print the data of dictionary
    print("\nPeople1:", data['people1'])
    print("\nPeople2:", data['people2'])

# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
#
# print(json.dumps("\"foo\bar"))
# print(json.dumps('\u1234'))
#
# print(json.dumps('\\'))
# from io import StringIO
# io = StringIO()
# json.dump(['streaming API'], io)
# io.getvalue()
