
# Parent Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        print(f" Calling {number} from {self.model}...")

    def show_specs(self):
        print(f" {self.brand} {self.model} - Battery: {self.battery_life} hours")

# Child Class: GamingPhone (Inheritance & Encapsulation)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system  # Extra feature

    def gaming_mode(self):
        print(f"🎮 {self.model} is now in Gaming Mode with {self.cooling_system} cooling!")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S22", 20)
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 24, "Advanced Liquid Cooling")

# Using methods
phone1.show_specs()
phone1.make_call("123-456-7890")

gaming_phone.show_specs()
gaming_phone.gaming_mode()
