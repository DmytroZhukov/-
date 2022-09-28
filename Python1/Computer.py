class PC:
    def __init__(self, memory: str = "2gb", harddrive: str = "500gb", model: str = "huawei", CPU: str = "AMD ryzen"):
        self.memory = memory
        self.harddrive = harddrive
        self.model = model
        self.CPU = CPU

    def __str__(self):
        return f"({self.memory}, {self.harddrive}, {self.model}, {self.CPU})"


class Board:
    def __init__(self, monitor: str = "монитор samsung", keyboard: str = "клава 4tech", mouse: str = "мышь 4tech", size: str = "размеры:30x50x20"):
        self.monitor = monitor
        self.mouse = mouse
        self.keyboard = keyboard
        self.size = size

    def desktop(self):
        print(
            f"Настольный компьютер: {self.monitor}, {self.mouse}, {self.keyboard}, {self.size}")


class Nout:
    def __init__(self, diagonal: str = "17 дюймов", size: str = "Габарины 25x15x1 см"):
        self.diagonal = diagonal
        self.size = size

    def noutbuk(self):
        print(f"Ноутбук: {self.diagonal}, {self.size}")


show = Board()
print(show.monitor)
show.desktop()
see = Nout()
see.noutbuk()
