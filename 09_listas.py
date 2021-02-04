animales=['Perro','Ornitorrinco','Gato','Canario','Ornitorrinco']
print(animales)
print(animales[0])
print(animales[1:2])
print(animales[:2])

i = animales.index('Ornitorrinco')
print(i)

animales[i] = 'Koala'
print(animales)

animales.append('Tortuga')
animales.insert(2,'Liebre')
print(animales)


animales.remove('Gato') ##Aliminar un registro 
item=animales.pop(1)
print(animales)
print(item)

cadena = 'Un anillo para gobernarlos a todos'

lista= cadena.split (' ')
print (lista)
lista.reverse() #Mostrar los elementos al reves
cadena2 = ''.join(lista)
print(cadena2) 


##Tuplas
tanimales = tuple(animales)
print (tanimales)
#print(tanimales.index('Gato'))
#print('Gato' in tanimales)