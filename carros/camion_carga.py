from auto import Auto


class CamionCarga(Auto):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "diiesel")

    def vidrios(self, estado):
        return f"Los vidrios estan {estado} y solo tiene vidrios en la cabina"

    def retrovisores(self, estado):
        return f"Los retrovisores estan {estado} y son grandes para ver los puntos ciegos"
