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


car1 = Car("BMW", "x6", "black", 50000)
car2 = Car("Toyota", "Camry", "silver", 40000)

# print(car1.maker)
# print(car1.price)
# car1.set_discount(0.25)
# print(car1.get_price())
print(car2.maker)
print(car2.price)
car2.set_discount(0.25)
print(car2.get_price())
