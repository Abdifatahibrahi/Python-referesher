
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a '{car.__class__.__name__}' to the garage, but you can only add 'Car' object ")
        self.cars.append(car)
ford = Garage()
car = Car("fosta", "fiesta")
ford.add_car(car)
ford.add_car("car2")
print(len(ford))