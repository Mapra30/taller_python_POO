from vivo import Vivo


class Abeja(Vivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "colmenar", "polen y nectar", tamano, color)

    def mover(self):
        return f"{self.nombre} vuela de flor en flor"

    def adaptarse(self):
        return f"{self.nombre} se adapta a las flores con su proboscis"
