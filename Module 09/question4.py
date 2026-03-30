import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

# Create 10 cars
cars = []
for i in range(1, 11):
    registration = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(registration, max_speed))

# Race loop
hour = 0
while True:
    hour += 1
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            break
    break

# Print results
print(f"Race finished after {hour} hours!\n")
print(f"{'Reg. number':<12} {'Max speed':>10} {'Curr. speed':>14} {'Distance':>10}")
print("-" * 50)
for car in sorted(cars, key=lambda c: c.travelled_distance, reverse=True):
    print(f"{car.registration_number:<12} {car.max_speed:>5} km/h "
          f"{car.current_speed:>5} km/h "
          f"{car.travelled_distance:>10.1f} km")