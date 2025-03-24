
# Parent Class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Child Classes with Polymorphism
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚢 The boat is sailing on water.")

# Using Polymorphism
vehicles = [Car(), Plane(), Boat()]  # List of different vehicle objects

for v in vehicles:
    v.move()  # Calls the specific move() method for each class
