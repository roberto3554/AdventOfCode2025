pos = 50
cont = 0

with open ('input.txt', 'r') as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    direccion = linea[0]
    pasos = int(linea[1:])
    pos += pasos if direccion == 'R' else -pasos
    pos %= 100
    if pos == 0: cont += 1

print(cont)