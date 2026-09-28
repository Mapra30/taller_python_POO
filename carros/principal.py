from auto import Auto
from deportivo import Deportivo
from camioneta import Camioneta
from camion_carga import CamionCarga

coche_deportivo = Deportivo("Deportivo", "negro", "3.5", 2, 2)
camioneta_blanca = Camioneta("Camioneta", "blanca", "2.8", 4, 5)
camion_carga = CamionCarga("Camion de carga", "blanco", "6.5", 2, 3)

print(coche_deportivo.encender())
print(coche_deportivo.acelerar_frenar("acelerar", 140))
print(coche_deportivo.acelerar_frenar("frenar", 70))
print(coche_deportivo.detener())
print(coche_deportivo.direccion("asistida"))
print(coche_deportivo.aire_acondicionado("encendido"))
print(coche_deportivo.seguridad())
print(coche_deportivo.faros("encendidos"))
print(coche_deportivo.vidrios("bajados"))
print(coche_deportivo.retrovisores("plegados"))

print(camioneta_blanca.encender())
print(camioneta_blanca.vidrios("cerrados"))
print(camioneta_blanca.seguridad())

print(camion_carga.encender())
print(camion_carga.vidrios("cerrados"))
print(camion_carga.retrovisores("abiertos"))
