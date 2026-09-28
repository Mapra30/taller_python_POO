class Auto:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
        self.marcha = False
        self.velocidad = 0

    def encender(self):
        self.marcha = True
        return f"Se enciende el {self.modelo}"

    def detener(self):
        self.marcha = False
        self.velocidad = 0
        return f"Se detiene el {self.modelo}"

    def acelerar_frenar(self, accion, velocidad):
        verbos = {"acelerar": ("acelera", velocidad), "frenar": ("frena", -velocidad)}
        verbo, cambio = verbos[accion]
        self.velocidad += cambio
        return f"El {self.modelo} {verbo} y marca {self.velocidad} km/h"

    def direccion(self, tipo):
        return f"Maneja con direccion {tipo}"

    def aire_acondicionado(self, estado):
        return f"El aire acondicionado esta {estado}"

    def seguridad(self):
        return "Trae cinturones y bolsa de aire"

    def faros(self, estado):
        return f"Los faros estan {estado}"

    def vidrios(self, estado):
        return f"Los vidrios estan {estado}"

    def retrovisores(self, estado):
        return f"Los retrovisores estan {estado}"
