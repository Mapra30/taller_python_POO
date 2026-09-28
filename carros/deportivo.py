from auto import Auto


class Deportivo(Auto):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "gasolina")

    def seguridad(self):
        return "Trae ABS, seis bolsas de aire y control de traccion"

    def direccion(self, tipo):
        return f"Maneja con direccion {tipo} muy respuesta"
