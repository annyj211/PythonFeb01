cadena = 'Un anillo para gobernarlos a todos'
l_c = len(cadena)
lista = cadena.split(' ')
print(lista)
print(len(lista))
print(l_c)
print(lista[0])
print(cadena[0])
lista[0]= 'El'
print(lista)
# cadena[0] = 'E' Genea error 
print(cadena[-1])
print(cadena[3:9]) # obtener fragmentos de la cadena 
print(cadena[10:])
print(cadena.count('a'))