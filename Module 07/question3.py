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
        print(airport_details[icao_code])

    choose = input("\nWhat do you choose? (new/fetch/quit): ")

else:
    print("Execution Ends!")