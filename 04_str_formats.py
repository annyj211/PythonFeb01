x = 'cadena de "caracteres" en \'Phyton\''
y = "Cadena de 'caracteres' \nen dos lineas"
# indicar que continua la linea \
z = 'Cadena de caracteres\n' + \
'en dos lineas'
m = '''Cadena de "caracteres"
en 'dos' lineas ❤''' # Todo lo que se haga dentro de los 
# ''' se mantiene  (srting de tipo template)
 
print(x)
print(y)
print(z) 
print(m) 
#x,y,z,m objetos, conjunto que tienen propiedades y se conocen como metodos y hacen parte del objeto

a='hola'
b= 'Hola mundo'
print(a.upper())
print(a.capitalize())
print(a.lower())
print(b.title())

cad = 'cadena de "caracteres" en Phyton' 
lista = cad.split(' ') #Separador de los elementos
print(lista)
lista.reverse()    #Metodos propios de los array
print(lista)
#Las cadena ya lleva los metodos, solo los debo llamar con a. cad. 
print(a.upper().startswith('H')) #Preguntar con que inicia la cadena
print(cad.strip())