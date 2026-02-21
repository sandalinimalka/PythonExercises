name_list = set()

name_input = input("Enter a name: ")

while name_input != "":
    if name_input in name_list:
        print("Existing name")
    else:
        print("New name")
    name_list.add(name_input)
    name = input("Enter a name: ")

print("\nName List: ")

for name in name_list:
    print(name)