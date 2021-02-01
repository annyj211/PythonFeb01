x= 3
print(x,type(x),id (x)) 
#direccion de la ubicacion de la memoria, todos son objetos que tiene su propia id

l= ['Pepe','Juan','Elena']
print(l, type(l), id (l))
#Variables son inmutables-> implica que se debe tener una referencia nueva
x= 23
print(x,type(x),id (x)) 

#Variables mutables => cambian sin cambiar sin referencia 
l[0]='Jose'
print(l, type(l), id (l))

# cambia el valor de la referencia, esto tiene importancia cuando copiamos elementos 
l= ['Pepe','Juan','Elena']
print(l, type(l), id (l))