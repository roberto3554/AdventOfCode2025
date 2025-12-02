cont = 0

def es_invalido(valor):
    longitud = len(valor)
    for i in range(1, longitud//2 + 1):
        if longitud % 1 != 0: continue
        bloque = valor[:i]
        if bloque * (longitud // i) == valor: return True
    return False

with open ('input.txt', 'r') as archivo:
    linea = archivo.readline()

lineas = linea.split(',')

for linea in lineas:
    inicio, fin = map(int, linea.split('-'))
    for i in range(inicio, fin + 1):
        if es_invalido(str(i)):
            cont += i

print(cont)