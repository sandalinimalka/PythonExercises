numbers = []
value = input("Enter a number: ")

while value != "":
    numbers.append(int(value))
    value = input("Enter a number: ")
numbers.sort(reverse=True)
print("Greatest five numbers are: " ,numbers[:5])
