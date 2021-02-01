# tengo 1 solo objeto con la referencia
x = 2
y = x
z = 2

print(x, id(x))
print(y, id(y))
print(z, id(z))

y = 5

print(x, id(x))
print(y, id(y))
print(z, id(z))

l1= ['Pepe','Juan','Elena']
l2= l1 # tener 2 referencias a la misma lista 
print(l1, id (l1))
print(l2, id (l2))

l1[0]='Jose' # cambia el valor a la lista
print(l1, id (l1))
print(l2, id (l2))

#clonado  [*l1]
l3 = [*l1]
l1[1]='Juanito'
print(l1, id (l1))
print(l3, id (l3))
