length_str = input("Enter the Length of Rectangle: ")
width_str = input("Enter the Width of Rectangle: ")

length = float(length_str)
width = float(width_str)

perimeter = (2 * (length + width))
area = (length * width)

print("Perimeter is  " + str(perimeter))
print("Area is " + str(area))