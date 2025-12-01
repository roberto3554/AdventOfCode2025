pos = 50
cont = 0

with open ('input.txt', 'r') as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    direccion = linea[0]
    pasos = int(linea[1:])
    if direccion == 'R':
        for i in range(pasos):
            pos += 1
            if pos == 0: cont += 1
            else:
                pos %= 100
                if pos == 0: cont += 1
    if direccion == 'L':
        for i in range(pasos):
            pos -= 1
            if pos == 0: cont += 1
            else:
                pos %= 100
                if pos == 0: cont += 1

print(cont)