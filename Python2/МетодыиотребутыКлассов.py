class Car:
    PURCHASE_TYPES = ("LEASE", "CASH")

    __sales_list = None

    @classmethod
    def get_purchase_types(cls):
        return cls.PURCHASE_TYPES

    @staticmethod
    def get_sales_list():
        if Car.__sales_list == None:
            Car.__sales_list = []
        return Car.__sales_list

    def __init__(self, maker, model, colour, price, purchase_type):
        self.maker = maker
        self.model = model
        self.colour = colour
        self.price = price
        if (not purchase_type in Car.PURCHASE_TYPES):
            raise ValueError(f"{purchase_type} is not a valid purchase type")
        else:
            self.purchase_type = purchase_type

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


car1 = Car("BMW", "x6", "black", 50000, "CASH")
car2 = Car("Toyota", "Camry", "silver", 40000, "LEASE")

print("Purchese types: ", Car.get_purchase_types())

print(car1.purchase_type)
print(car2.purchase_type)

sales_this_month = Car.get_sales_list()
sales_this_month.append(car1)
sales_this_month.append(car2)
print(sales_this_month)


# boat1 = Boat("Titanic")

# print(type(car1))
# print(type(boat1))
# print(type(car1) == type(boat1))

# Определение типа обьекта и проверка ;
# Проверка является ли обьект экремпляром класса.

# print(isinstance(car1, Car))
# print(isinstance(boat1, Boat))
# print(isinstance(boat1, Car))
# print(isinstance(car1, Boat))

# print(isinstance(car1, object))
# print(isinstance(boat1, object))
