airport_details = {"EFEJ" : "Espoo",
                   "EFLA" : "Lahti",
                   "EFHK" : "Helsinki - Vantaa",
                   "EFHO" : "Oulu",
                   "EFPT" : "Tampere"}

choose = input("What do you choose? (new/fetch/quit): ")

while choose != "quit":
    if choose == "new":
        icao_code = input("Enter ICAO code: ")
        airport_name = input("Enter airport name: ")
        airport_details[icao_code] = airport_name

    elif choose == "fetch":
        icao_code = input("Enter ICAO code: ")
        if icao_code in airport_details:
            print(airport_details[icao_code])
        else:
            print("ICAO Code not found!")

    choose = input("\nWhat do you choose? (new/fetch/quit): ")

print("Execution Ends!")