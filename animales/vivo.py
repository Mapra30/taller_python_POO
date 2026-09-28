class Vivo:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color

    def mover(self):
        return f"{self.nombre} se mueve en su {self.habitat}"

    def avisar(self):
        return f"{self.nombre} avisa a los demas como se siente"

    def reproducir(self):
        return f"{self.nombre} tiene crias"

    def comer(self):
        return f"{self.nombre} come {self.dieta}"

    def adaptarse(self):
        return f"{self.nombre} se acostumbro a su {self.habitat}"

    def reflejos(self):
        return f"{self.nombre} reacciona rapido por instinto"

    def descansar(self):
        return f"{self.nombre} descansa en su {self.habitat}"

    def dormir(self):
        return f"{self.nombre} duerme toda la noche"

    def socializar(self):
        return f"{self.nombre} convive con los de su {self.habitat}"
