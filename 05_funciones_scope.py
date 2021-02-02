#Dentro de una función son locales y fuera de la función son globales
def prueba(c):
    c='Juan'
    d='Pedro'
    print('Dentro de la funcion c vale:', c) #Variables locales
    print('Dentro de la funcion d vale:', d)
    print('Dentro de la funcion d vale:', a)

c = 'Carlos'
a = 'Ernesto' #Variables globales
prueba('')
print('fueraa de la funcion c vale:', c)
print('fueraa de la funcion c vale:', a)
#print('Dentro de la funcion c vale:', d) Genera error 

###################### ---Manejando Arrays--- ######################

def prueba_lista(c):
    c[0]='Juan'
    print('Dentro de la funcion c vale:', c) #Variables locales
 

c = ['Carlos','Maria']

#prueba_lista(c) #no puedo enviar solo el objeto c porque reemplaza lo que hay en la función
prueba_lista([*c]) #Debo clonar para que no se pierda el dato de la función local
print('Fuera de la funcion c vale:', c)
#print('Dentro de la funcion c vale:', d) Genera error 