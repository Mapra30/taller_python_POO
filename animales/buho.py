from vivo import Vivo


class Buho(Vivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "bosque de noche", "ratones", tamano, color)

    def mover(self):
        return f"{self.nombre} vuela sin hacer ruido"

    def reflejos(self):
        return f"{self.nombre} ve mejor en la oscuridad"
