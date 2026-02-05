inches = 0

while inches >= 0:
    inches = float(input("Enter inches: "))

    while inches >= 0:
        centimeters = inches * 2.54
        print(f"{inches} inches = {centimeters} centimeters")
        inches = float(input("Enter inches: "))
