lenguaje = 'Python'
autor = 'Guido'

msg = 'El lenguaje ' + lenguaje + ' fue creado por ' + autor
print(msg)

mi_msg =  'El lenguaje {} fue creado por {}'.format(lenguaje, autor) #Aqui si imprime en ese orden 
print(mi_msg)

i_msg = 'El lenguaje {leng} fue creado por {autor}'.format(leng=lenguaje, autor=autor) # no interesa el orden
print(mi_msg)


i_msg = 'El lenguaje %s fue creado por %s' % (lenguaje, autor) 
print(mi_msg)


i_msg = 'El lenguaje {lenguaje} fue creado por {autor}'
print(mi_msg)