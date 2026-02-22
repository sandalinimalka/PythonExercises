import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'sandalk',
    password = 'sandalk123',
    autocommit = True
)

def airport_details_by_country_code(country_code):
    sql = f"""SELECT country.name, airport.type, count(airport.type) AS 'airport_count'
            FROM airport
            LEFT JOIN country ON airport.iso_country = country.iso_country
            WHERE airport.iso_country = '{country_code}'
            GROUP BY airport.type
            ORDER BY airport.type"""
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[0]} has {row[2]} {row[1]} airports")

area_code = input("Enter the area code: ")
airport_details_by_country_code(area_code)
