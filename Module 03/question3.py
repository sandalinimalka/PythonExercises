gender = input("What is your gender? male/female: ")
hemoglobin_value = float(input("What is your hemoglobin value (g/l)?: "))

if gender == "female" :
    if hemoglobin_value < 117:
        print("Hemoglobin Value is Low")
    elif hemoglobin_value > 155:
        print("Hemoglobin Value is High")
    else:
        print("Hemoglobin Value is Normal")
else:
    if hemoglobin_value < 134:
        print("Hemoglobin Value is Low")
    elif hemoglobin_value > 167:
        print("Hemoglobin Value is High")
    else:
        print("Hemoglobin Value is Normal")