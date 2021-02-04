def read_file(fname):
    try:
        f = open(fname,'rt') #Genera error
        text = f.read()
    except FileNotFoundError:
        text = f'No existe el fichero{fname} en el directorio'
    return text

print(read_file('sample.txt'))   
print(read_file('sample2.txt'))   



