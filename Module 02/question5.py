talents_str = input("Enter Talents: ")
pounds_str = input("Enter Pounds: ")
lots_str = input("Enter Lots: ")

talents = float(talents_str)
pounds = float(pounds_str)
lots = float(lots_str)

total_pounds = (talents * 20) + pounds
total_lots = (total_pounds * 32) + lots
total_grams = (total_lots * 13.3)

total_kilograms = int(total_grams / 1000)
total_remaining_grams = (total_grams % 1000)

print()
print("The weight in modern units: ")
print(f"{total_kilograms} kilograms and {total_remaining_grams:.2f} grams.")