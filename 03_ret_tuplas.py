l=['Pepe','Juan','Elena']
t=('Pepe','Juan','Elena') #Las tuplas no aceptan nuevos registros despues de ser definidos, no puedo aumentar o eliminar registros 

l[0]= 'Juan'
l.append('Luis')

print(l)#Imprimir el array, puedo agregar o modificar elementos 
t=(1,2,3,1,1,2)
print(t,len(t)) #len es funcion independiente
print(t.count(1))
