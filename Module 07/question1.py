month_number = int(input("Enter a number of a month(1-12): "))

seasons = ("Winter", "Spring", "Summer", "Autumn")

season_index = int((month_number % 12) / 3)

print(f"Month {month_number} is in the {seasons[season_index]} season.")