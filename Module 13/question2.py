from flask import Flask

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='sandalk',
    password='sandalk123',
    autocommit=True
)

app = Flask(__name__)

@app.route("/airport/<icao>", methods=["GET"])
def airport(icao):
    icao = icao.upper()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()

    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        response = {
            "ICAO": icao,
            "Name": result[0],
            "Location": result[1]
        }
        return response, 200
    else:
        response = {
            "error": "airport not found"
        }
        return response, 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
