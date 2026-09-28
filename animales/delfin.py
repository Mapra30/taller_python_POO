from vivo import Vivo


class Delfin(Vivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "mar abierto", "peces", tamano, color)

    def mover(self):
        return f"{self.nombre} nada rapido y salta fuera del agua"

    def adaptarse(self):
        return f"{self.nombre} se adapta al mar con sus aletas y su cola"
