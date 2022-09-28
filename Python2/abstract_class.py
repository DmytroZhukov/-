# ABC = Abstract Base class
from abc import ABC, abstractmethod


class Electrical_Appliance(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def electricity_consumption(self):
        pass


class Heater(Electrical_Appliance):
    def __init__(self, heating):
        self.heating = heating

    def electricity_consumption(self):
        return 1500 * self.heating


class Cooler(Electrical_Appliance):
    def __init__(self, cooling):
        self.cooling = cooling

    def electricity_consumption(self):
        return 300 * self.cooling


# e = Electrical_Appliance()
h = Heater(50)
print(h.heating, h.electricity_consumption())
c = Cooler(20)
print(c.cooling, c.electricity_consumption())
