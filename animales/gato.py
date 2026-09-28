from vivo import Vivo


class Gato(Vivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "casa", "atun", tamano, color)

    def mover(self):
        return f"{self.nombre} camina sin ruido y salta"

    def avisar(self):
        return f"{self.nombre} avisa con maullidos"
