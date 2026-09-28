from vivo import Vivo
from gato import Gato
from delfin import Delfin
from buho import Buho
from abeja import Abeja
from vaca import Vaca

gato = Gato("Michi", 3, "pequeno", "gris")
delfin = Delfin("Delfin", 8, "mediano", "gris claro")
buho = Buho("Buho", 5, "mediano", "cafe")
abeja = Abeja("Abeja", 1, "muy pequena", "amarillo y negro")
vaca = Vaca("Vaca", 6, "grande", "blanca con manchas")

print(gato.mover())
print(gato.avisar())
print(gato.reproducir())
print(gato.comer())
print(gato.adaptarse())
print(gato.reflejos())
print(gato.descansar())
print(gato.dormir())
print(gato.socializar())

print(delfin.mover())
print(delfin.adaptarse())

print(buho.mover())
print(buho.reflejos())

print(abeja.mover())
print(abeja.adaptarse())

print(vaca.mover())
print(vaca.avisar())
