number = int(input("Enter a number: "))
is_prime_number = True

for i in range(2,number):
    if number % i == 0:
        is_prime_number = False
        break

if is_prime_number:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

