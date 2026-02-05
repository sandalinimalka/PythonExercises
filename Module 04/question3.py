smallest = 0
largest = 0

number = input("Enter a number: ")
if number != "": smallest = float(number)

while number != "":
    value = float(number)
    if value> largest:
        largest = value
    if value < smallest:
        smallest = value
    number = input("Enter a number: ")

print("Smallest number:", smallest)
print("Largest number:", largest)