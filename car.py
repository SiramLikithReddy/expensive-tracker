#car
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        print(f"You're car name: {self.name}")
        print(f"You're speed: {self.speed}")

    def fuel(self):
        try:
            fuel = int(input("Enter the existing fuel% : "))
            print(f"Existing fuel%: {fuel}")
        except ValueError:
            print("check you're datatype")
        return fuel

t = Car("Tata", 160)
print(t.fuel())

with open("cars.py", "a") as file:
    file.write(f"Good {t.name} car\n")