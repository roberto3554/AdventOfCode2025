cont = 0

with open ('input.txt', 'r') as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    primero = max(linea[:-2])
    pos_primero = linea.find(primero)
    segundo = max(linea[pos_primero+1:-1])

    cont += (int(primero) * 10 + int(segundo))

print(cont)
