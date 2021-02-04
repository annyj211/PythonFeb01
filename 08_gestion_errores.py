def dividir(a,b):
    try: #Aquí debería encontrar todas las excepciones, todos los errores que preveemos, los errores deben pasar silenciosamente, controlarlos
        return a / b
    except ZeroDivisionError:
        print('No se puede dividir por cero')   
    except Exception as err:
        print ('Error',type(err).__name__) #__name__ Variables de uso interno, nombre de la clase a la que pertenece

print(dividir(7,2))

r=(dividir(7,0))  #No es posible dividir por cero
if r != None:  print(r) # Cuando es None no imprime nada


try: ##Try en la llamada a las funciones
    print(dividir(7))
except TypeError as err:
        print ('Error',type(err).__name__)

