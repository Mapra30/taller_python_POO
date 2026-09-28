from auto import Auto


class Camioneta(Auto):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "diesel")

    def vidrios(self, estado):
        return f"Los vidrios estan {estado} y atras hay lugar para carga"

    def seguridad(self):
        return "Trae camara de retroceso y bolsas de aire"
