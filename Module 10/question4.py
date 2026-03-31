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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.hours_elapsed = 0

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
        self.hours_elapsed += 1

    def print_status(self):
        print(f"\n{'─' * 58}")
        print(f"  {self.name}  |  Hour: {self.hours_elapsed}  |  Distance: {self.distance} km")
        print(f"{'─' * 58}")
        print(f"  {'Reg. number':<12} {'Max speed':>10} {'Curr. speed':>12} {'Distance':>12}")
        print(f"{'─' * 58}")
        for car in sorted(self.cars, key=lambda c: c.travelled_distance, reverse=True):
            driven = min(car.travelled_distance, self.distance)
            status = f"{driven:>10.1f} km"
            print(f"  {car.registration_number:<12} {car.max_speed:>7} km/h "
                  f"{car.current_speed:>7} km/h {status:>12}")
        print(f"{'─' * 58}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


# Main program
cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)
print(f"Race started: {race.name} — {race.distance} km, {len(race.cars)} cars!")

while not race.race_finished():
    race.hour_passes()
    if race.hours_elapsed % 10 == 0:
        race.print_status()

race.print_status()

# Print results
print(f"\nRace finished after {race.hours_elapsed} hours!\n")

