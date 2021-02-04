animales=['Perro','Ornitorrinco','Gato','Canario','Ornitorrinco'] #Frecuente que los arrays se llamen en plurarl

i = 0
for animal in animales: ##Es recomendable llmar la variable igual que el array pero en singular
    if animal.lower() == 'Ornitorrinco':
        continue ## De este modo me salto la vuelta, no hace que se pare el bucle
    print(animal)


print('============================')
## Alternativa a continue es break

passw = 'Ornitorrinco'
userPass = ''
i = 1
while (userPass != passw):
    userPass = input('Escriba la contraseña: ')
    if i >= 3:
        print('Demasiados12 intentos')
        break
    i += 1
else:                ## Elementos que queremos que se cumpla si se cumple la condición 
    print('Saludo, ya estas dentro')