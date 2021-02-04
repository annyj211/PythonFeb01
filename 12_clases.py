class persona(): #Definicipn de la clase
    ###similar a constructor, se define de la sgte forma:
    #Se debe hacr explicita como los primeros parametros del onstructor
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        #self.altura #no quiero definir un valor para altura
        self.__estudios = None #__Parametro protegido
#Capaz de acceder al self para obtener la información del objeto
#Todos los metodos deben tener definido un parametro
    def saludar(self):
        print(f'Hola soy {self.nombre}, y tengo {self.edad} anos') 
     def saludar_a(self,alguien = 'amigo'):
        print(f'Hola {alguien}, soy {self.nombre}, y tengo {self.edad} anos')        

############## #Uso de la clase 
p1 = persona('Pepe',22)
p2 = persona('Elena',32)

print(type(p1),p1.nombre)
print(type(p2),p2.nombre)
p1.saludar()
p1.saludar_a(p1.nombre)

print(p1.edad) #No se debe
#print(p1__estudios) #AttributeError: No se puede acceder
print(p1.Persona__estudios) #.... o si, acceder de forma especial

p1.nombre = 'Jose'
print(p1.nombre)

p1.edad = 24
print (p1.nombre,p1._dad)

p1._Persona__estudios = 'Informatica'
print (p1._Persona__estudios)

p1.altura = 180
print(p1.altura)

print(isinstance)