from vivo import Vivo


class Vaca(Vivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "pradera", "hierba", tamano, color)

    def mover(self):
        return f"{self.nombre} camina lento y come pasto"

    def avisar(self):
        return f"{self.nombre} avisa con mugidos"
