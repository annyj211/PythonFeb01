print(3 + 4)
print(3 - 4)
print(3 * 4)
print(4 // 3) #Division entre enteros //, resultado con decimales
print(3 % 4) #Operador Mod división
print(3 ** 4)#Exponenciación 
print((3 + 4) * 2)

x = 8
x += 2 # x = x + 2

d = 0
e = 2 

print(d == e) # Comparando se realiza con ==
print(d != e) # Diferencia !=
print(d > e) #Mayor
print(d >= e) #Mayor Igual
print(d < e) #Menor 
print(d <= e) #Menor Igual

print ('Pepe'< 'Valeria')

a = [1,2,3]
a1 = a
b = [1,2.3]

print (a == a1)
print (a == b)

print (id(a))
print (id(a1)) #Misma referencia con a
print (id(b)) #Diferente referencia

print (a is a1) #Si son iguales
print (a is b) #Desigualdad, cada uno nació por separado

### And-OR-NOT ###

d = 0
e = 2
a = 10

print('AND:',a != d and d > e) 
print('AND:', d > e and a != d) #la segunda comparacion no se ejecuta
print('OR:', a != d or d > e) #Si la primera se cumple ya no ejecuta la otra
print('OR:', d > e  or a != d)

print(12 and 23) #Toma el ult valor
print(12 or 23) #Toma el primer valor

def suma(a,b): #Parametros
    r = a + b
    return r 

print (a == b and suma(2,34))
print (a != b and suma(2,34)) # Podemos combinar operadores y ejecutar la funcion
# Es decir que si se cumple la condición se ejecute la función

print('OR:',a != d and d > e) 
print('OR:',a != d and not d > e) 

print (not 'Pepe')


