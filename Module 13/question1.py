from flask import Flask, request

app = Flask(__name__)

@app.route("/prime_number/<int:number>")
def prime_number(number):
    is_prime_number = True
    if number < 2:
        is_prime_number = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime_number = False
                break

    response = {
        "Number" : number,
        "isPrime" : is_prime_number
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host = '127.0.0.1', port = 5000)