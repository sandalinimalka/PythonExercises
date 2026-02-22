import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'sandalk',
    password = 'sandalk123',
    autocommit = True
)

def airport_details_by_icao_code(ident):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{ident}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport Name: {row[0]}, Location: {row[1]}")
    return

ident_input = input("Enter the ICAO Code: ")
airport_details_by_icao_code(ident_input)

