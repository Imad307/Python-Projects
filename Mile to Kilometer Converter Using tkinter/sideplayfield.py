def add(*my_tuple):
    result = 1
    for num in my_tuple:
        result*= num
    return result

print(add(1, 2, 3))


class Car:
    def __init__(self, **kw):
        self.model = kw.get("model")
        self.make = kw.get("make")
        self.color = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Suzuki", model="Mehran", colour="white", seats=4)

print(my_car.model, my_car.seats, my_car.make, my_car.color)