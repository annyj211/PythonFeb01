def suma(a= 0, b=0):# parámetros
    r = a+b
    return r

def resta(a= 0, b=0):# parámetros
    r = a-b
    return r    

print(type(suma))

 #Si pertenece a una clase es un objeto, ref que apunta a un espacio de memory
 #Las funciones no tienen metodo de clonación

y=suma
print(y(3,5))

#Callback funciones asincronas, necesitamos que le llegue info para que se pueda ejecutar
#Callback No te paso el resultado de la suma, te paso la funcion suma para que realices la suma
def calcular(a, b, callback ):
    print(callback(a,b))

calcular(3,8, suma)
calcular(3,8, resta)
calcular(3,8, lambda a,b: a*b) #lambda, funciones anonimas

div= lambda a,b: a/b
print(div(3,5))

def multiplicador(n):
    return lambda a: a * n

duplicar = multiplicador(2)    
triplicar = multiplicador(3)   

print(duplicar(12))
print(triplicar(12))