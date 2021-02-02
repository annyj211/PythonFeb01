#Declaracion de la función
def sumaOk(a,b): #Parametros
    r = a + b
    return r 
#Mala practica por mezclar funcionalidades se debería hacer funciones limpias 
def suma(a,b):
    def sum(a,b):
        return a+b
    r = a + b
    print(r)  
print(type(suma))

indice = 6
#Llamar la función    
print(sumaOk(3,indice)) #pasamos argumentos
print(suma(50,18))

def sumaOkDef(a=0,b=0): #Para evitar errores defino valores por defecto
    r = a + b
    return r 

print(sumaOkDef(50))  
print(sumaOkDef())    

def resta(a=0,b=0): #Para evitar errores defino valores por defecto
    r = a - b
    return r 

print(resta(50,10))
print(resta(50))  
print(resta()) 