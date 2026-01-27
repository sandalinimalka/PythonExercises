year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It is a Leap Year")
elif year % 100 == 0:
    print("It is not a Leap Year")
elif year % 4 == 0:
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")