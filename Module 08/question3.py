import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'sandalk',
    password = 'sandalk123',
    autocommit = True
)

def calculate_distance (code1, code2):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connection.cursor()

    cursor.execute(sql, (code1,))
    result1 = cursor.fetchone()

    cursor.execute(sql, (code2,))
    result2 = cursor.fetchone()

    coord1 = (result1[0], result1[1])
    coord2 = (result2[0], result2[1])

    return distance.distance(coord1, coord2).kilometers

first_ident = input("Enter the First ICAO Code: ")
sec_ident = input("Enter the Second ICAO Code: ")

result = calculate_distance(first_ident, sec_ident)

print(f"Distance between {first_ident} and {sec_ident}: {result:.2f} KM")