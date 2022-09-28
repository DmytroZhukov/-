class Car:
    def __init__(self, maker, model, colour, price):
        self.maker = maker
        self.model = model
        self.colour = colour
        self.price = price

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount


class Boat:
    def __init__(self, name):
        self.name = name


car1 = Car("BMW", "x6", "black", 50000)
car2 = Car("Toyota", "Camry", "silver", 40000)

boat1 = Boat("Titanic")

# print(type(car1))
# print(type(boat1))
# print(type(car1) == type(boat1))

# Определение типа обьекта и проверка ;
# Проверка является ли обьект экремпляром класса.

print(isinstance(car1, Car))
print(isinstance(boat1, Boat))
print(isinstance(boat1, Car))
print(isinstance(car1, Boat))

print(isinstance(car1, object))
print(isinstance(boat1, object))
