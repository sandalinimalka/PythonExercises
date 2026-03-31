class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self,floor):
        if self.top_floor < floor or self.bottom_floor > floor:
            print(f"Invalid Floor Number! Please check Again,")
            return

        if self.current_floor < floor:
           for i in range(self.current_floor,floor):
                self.floor_up()

        else:
            for i in range(floor, self.current_floor):
                self.floor_down()

    def floor_up(self):
        self.current_floor += 1
        print(f"Current Floor: {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Current Floor: {self.current_floor}")

#question1
elevator = Elevator(1, 9)
print(f"---Going to Floor 5--- ")
elevator.go_to_floor(5)
print(f"---Going back to bottom floor---")
elevator.go_to_floor(elevator.bottom_floor)
print("-" * 30)
print()

#Create new building class
class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        self.num_elevators = num_elevators
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Elevator {elevator_number} does not exist.")
            return
        running_elevator= self.elevators[elevator_number - 1]
        print(f"---Elevator {elevator_number} → floor {destination_floor}---")
        running_elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("FIRE ALARM! All elevators returning to bottom floor.")
        for i in range(self.num_elevators):
            print(f"Elevator {i + 1} → floor {self.bottom_floor}:")
            running_elevator = self.elevators[i]
            running_elevator.go_to_floor(self.bottom_floor)

#question2
tower = Building(0, 10, 3)

tower.run_elevator(1, 7)
tower.run_elevator(2, 3)
tower.run_elevator(3, 10)
tower.run_elevator(1, 0)
print("-" * 30)
print()

#question3
tower.fire_alarm()