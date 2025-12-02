cont = 0

with open ('input.txt', 'r') as archivo:
    linea = archivo.readline()

lineas = linea.split(',')

for linea in lineas:
    inicio, fin = map(int, linea.split('-'))
    for i in range(inicio, fin + 1):
        valor = str(i)
        if len(valor) % 2 == 0 and valor[:len(valor)//2] == valor[len(valor)//2:]:
            cont += i

print(cont)