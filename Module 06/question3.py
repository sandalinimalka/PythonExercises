def gallons_to_litters(gallons):
    return gallons * 3.78541

gal_in_litters = 0
vol_gallons = int(input("Enter the volume of the gallons: "))
while vol_gallons > 0:
    gal_in_litters = gallons_to_litters(vol_gallons)
    print(f"{vol_gallons} gallon/gallons equals {gal_in_litters:.2f} litters")
    print()
    vol_gallons = int(input("Enter the volume of the gallons: "))


