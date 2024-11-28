class Transport:
    def __init__(self, weight, distance):
        self.weight = weight
        self.distance = distance

    def calculate_cost(self):
        pass

class Truck(Transport):
    def __init__(self, weight, distance):
        super().__init__(weight, distance)

    def calculate_cost(self):
        return self.weight * self.distance

class Ship(Transport):
    def __init__(self, weight, distance):
        super().__init__(weight, distance)

    def calculate_cost(self):
        return self.weight * self.distance

class Plane(Transport):
    def __init__(self, weight, distance):
        super().__init__(weight, distance)

    def calculate_cost(self):
        return self.weight * self.distance

truck = Truck(100, 10)
ship = Ship(500, 100)
plane = Plane(1000, 1000)

print(truck.calculate_cost())
print(ship.calculate_cost())
print(plane.calculate_cost())