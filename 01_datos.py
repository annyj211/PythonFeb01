#En Python el tipado es dinamico, pero fuerte. Si yo cambio el valor cambia el tipo de la variable
#el tipo de la variable puede cambiar en cualquier manera, depende del valor de la variable
#Tipos basicos
#str
x= 'Hola'
print(x,type(x))
#int
x=34
print(x,type(x))
#float
x=34.78
print(x,type(x))
#true o false 
x=True
print(x,type(x))
x=False
print(x,type(x))
#None
x=None
print(x,type(x))
#Tipos complejos
#[]Listas, array,Elementos indexados, indefinida en su longitud 
c=['Pepe',23, True]
print(c,type(c))
#()Tupla, array inmutable. No puedo agregar elementos o modificarlos 
c=('Pepe',23, True)
print(c,type(c))
#{} Set, array de unica representacion de elementos unicos. 
c={'Pepe',23, True}
print(c,type(c))
#{} Diccionario, array asociativos, hashes, objetos literales,javaobjects. 
#Coleccion de propiedades con valores
c={'nombre':'Pepe','edad':23, 'isAlumne':True}
print(c,type(c))