length = int(input("Enter the length of a Zander(in cm): "))
if length < 42:
    difference = 42 - length
    print("Release the fish back into the lake")
    print(f"It is {difference} cm below size limit")
else:
    print("The zander meets the size limit. You can keep it.")
