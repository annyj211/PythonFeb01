import modulo # Al importar globalmente un modulo, debo decirle que quiero usarlo, aquí nos proporsiona un espacio de nombre
import modulo as m #Pueso importar con un alias y usarlo

import package.modulo as mp

from modulo import suma, resta # si quireo importar solo una funcion del modulo 

from package.modulo import sust

print(modulo.suma(8,9))
print(m.suma(8,9))

print(suma(12,67))
print(suma(12,6))

print(mp.add(3,6))

print(sust(8,4,6))
