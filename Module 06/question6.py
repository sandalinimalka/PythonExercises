def pizza_unit_price(diameter, price):
    diameter_in_meters = diameter / 100
    radius = diameter_in_meters / 2
    area = (22/7) * (radius * radius)
    return  price / area

diameter1_input = float(input("Enter the diameter of the 1st pizza (in centimeters): "))
price1_input = float(input("Enter the price of the 1st pizza (in euros): "))

diameter2_input = float(input("\nEnter the diameter of the 2nd pizza (in centimeters): "))
price2_input = float(input("Enter the price of the 2nd pizza (in euros): "))

unit_price_pizza1 = pizza_unit_price(diameter1_input, price1_input)
unit_price_pizza2 = pizza_unit_price(diameter2_input, price2_input)

if unit_price_pizza1 < unit_price_pizza2:
    print(f"\n1st pizza provides better value for {price1_input:.2f} euros")
elif unit_price_pizza1 > unit_price_pizza2:
    print(f"\n2nd pizza provides better value for {price2_input:.2f} euros")
else:
    print(f"\nBoth pizzas provide better value for money.")