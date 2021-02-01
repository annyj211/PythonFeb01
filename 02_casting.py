x='12'
y= 3
z= 4
print(x,type(x))
print(y,type(y))
print(z,type(z))

print('y + z=', y + z ) 
# print('x + y', x + y )-> Error

#Tipado debi(JS) -> casting implicito 'x + y'=123 lo transforma a str
#Tipado fuerte: No hay casting implicito, es decir genera error
# #TypeError: can only concatenate str (not "int") to str
# se debe hacer el casting (es decir convertir el valor) para poder realizar la operacion. 

print ('x + y=', x + str(y))
print ('x + y=', int(x) + y) 

#Se sigue manteniendo el valor de la variable 
print(x,type(x))
print(y,type(y))
#En algunas ocasiones el casting lo hace automaticamente como en multiplicacion
# o en not
a = 12
b = 2.4
c = 0
print(a,type(a))
print(b,type(b))

print('a*b=', a*b)

print(not a) #not pasa los numeros a true
print(not c) #pero el cero si es false

print(not not a) #hace casting automatico a booblean
print(not not c) 

print(bool(a)) #El bool hace el casting implicito
print(bool(c))